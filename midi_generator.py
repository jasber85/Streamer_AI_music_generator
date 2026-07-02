import datetime
import shutil
from music21 import chord, instrument, stream, tempo
import numpy as np

# 導入前一步訓練好的模型與工具函數
from midi2audio import FluidSynth
from rnn_model import *
from song import convert_wav


def from_scratch(emotion, midi_num=MIDI_NUM):
    """當沒有輸入初始 MIDI 時，建立空白序列以進行「從頭盲創（From Scratch）」音樂生成。

    :param emotion (str): 當前想要生成的情緒標籤
    :param midi_num (int): 預計一次要生成的歌曲數量
    :return data (list): 包含多個空白列表的陣列（初始狀態）
    :return filenames (list): 結合當前時間與情緒所自動生成的檔案名稱列表
    """
    data = []
    filenames = []

    # 獲取當前 UTC 時間並格式化，避免檔名重複
    nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
    for midi_index in range(midi_num):
        data.append([])  # 放入空白序列作為生成的起點
        filenames.append(emotion + nowTime + "-" + str(midi_index + 1))

    return data, filenames


def sample(prediction, temperature=TEMPERATURE):
    """對模型輸出機率向量進行「溫度採樣（Temperature Sampling）」，控制音樂的創造力或規律性。

    :param prediction (ndarray): 模型預測下一個音符的 Softmax 機率分佈向量
    :param temperature (float): 溫度係數。越接近 0 越保守（只選機率最高）；越大越隨機瘋狂。
    :return index (int): 最終抽樣決定出的音符或和弦整數索引
    """
    # 透過數學計算調整機率分佈的陡峭度
    prediction = np.log(prediction) / temperature
    probabilites = np.exp(prediction) / np.sum(np.exp(prediction))

    # 依據調整後的機率分佈進行隨機抽樣
    index = np.random.choice(range(len(probabilites)), p=probabilites)

    return index


def generate_notes(model, data, emotion, filenames, a, max_notes=MAX_BARS):
    """利用音符 RNN 模型，以滑動視窗方式逐字預測並生成一連串音符。"""
    for index in range(len(data)):
        # 在開頭塞入長度為 SEGMENT_LENGTH 的填充符 '*'，模擬起始狀態
        song = ["*"] * SEGMENT_LENGTH + data[index]

        try:
            # 取出歌尾固定長度的音符，透過對應字典轉成整數編碼
            input_notes = [note2int[note] for note in song[-SEGMENT_LENGTH:]]
        except:
            print('Warning: Unknown notes found in "%s"' % filenames[index])
            continue

        midi_path = OUTPUTS_PATH + "\\" + filenames[index] + ".mid"
        print('Processing "%s"' % midi_path)

        output_note = None
        num_notes = 0

        # 當長度未達上限，且模型沒有抽到停止填充符 '*' 時，持續生成
        while (num_notes < max_notes or max_notes == 0) and output_note != "*":
            # 轉換為 One-hot 編碼，並新增一個維度（Batch size = 1）以符合 Keras 輸入格式
            one_hot_input = to_categorical(
                input_notes, num_classes=len(NOTE_TO_INT(emotion, a))
            )
            one_hot_input = one_hot_input[np.newaxis, ...]

            # 模型預測並進行採樣
            prediction = model.predict(one_hot_input)[0]
            note_index = sample(prediction)
            output_note = int2note[note_index]
            print(output_note)

            # 更新輸入視窗：丟棄最舊的音符，加入剛剛生成的新音符
            input_notes = input_notes[1:]
            input_notes.append(note_index)

            num_notes += 1
            if output_note != "*":
                song.append(output_note)

        # 回傳切除開頭填充符後，真正生成的音符序列
        return song[SEGMENT_LENGTH:]


def generate_chord(model, data, emotion, filenames, a, max_notes=MAX_BARS):
    """利用和弦 RNN 模型逐字預測並生成和弦序列（邏輯與生成音符完全相同）。"""
    for index in range(len(data)):
        song = ["*"] * SEGMENT_LENGTH + data[index]

        try:
            input_notes = [chord2int[note] for note in song[-SEGMENT_LENGTH:]]
        except:
            print('Warning: Unknown notes found in "%s"' % filenames[index])
            continue

        midi_path = OUTPUTS_PATH + "\\" + filenames[index] + ".mid"
        print('Processing "%s"' % midi_path)

        output_note = None
        num_notes = 0

        while (num_notes < max_notes or max_notes == 0) and output_note != "*":
            one_hot_input = to_categorical(
                input_notes, num_classes=len(CHORD_TO_INT(emotion, a))
            )
            one_hot_input = one_hot_input[np.newaxis, ...]

            prediction = model.predict(one_hot_input)[0]
            note_index = sample(prediction)
            output_note = int2chord[note_index]
            print(output_note)

            input_notes = input_notes[1:]
            input_notes.append(note_index)

            num_notes += 1
            if output_note != "*":
                song.append(output_note)

        # 除了回傳序列，也把預計輸出的 midi_path 一併帶回
        return song[SEGMENT_LENGTH:], midi_path


def convert_midi(notes, chords, midi_path, ins, bpm):
    """將模型生成的音符與和弦字串序列，解析並解碼回 music21 物件，最終寫入實體 MIDI 檔案。

    :param notes (list): 生成的音符字串序列（可能包含音高、延音符 '-'、休止符 '0'）
    :param chords (list): 生成的和弦字串序列
    :param midi_path (str): 輸出的目標 MIDI 檔案路徑
    :param ins (str): 使用者指定的樂器名稱（如 'piano', 'guitar'）
    :param bpm (int): 樂曲的速度（每分鐘節拍數）
    """
    midi_notes = []
    midi_chords = []
    pre_element = None
    duration = 0.0
    offset = 0.0

    # --- 第一部分：解碼主旋律音符 (Notes) ---
    for element in notes:
        if element != "-":  # 如果遇到新音符（不是延音符）
            if pre_element != None:
                if pre_element == "0":
                    new_note = note.Rest()  # '0' 代表休止符
                elif pre_element.startswith("["):
                    # 這一大段是字串解析邏輯，用來把字串形式的清單 "[60, 64, 67]" 解析成真實的整數串列
                    a = list(pre_element)
                    c = list(pre_element)
                    for i in range(0, len(a)):
                        if (
                            a[i] == "["
                            or a[i] == ","
                            or a[i] == "]"
                            or a[i] == " "
                        ):
                            c.remove(a[i])
                        elif a[i + 1].isdigit():
                            t = a[i] + a[i + 1]
                            c.remove(a[i])
                            c.remove(a[i + 1])
                            c.insert(i, t)
                    b = list(map(int, c))
                    b = list(set(b))
                    new_note = chord.Chord(b)  # 封裝成 music21 的和弦物件
                else:
                    new_note = note.Note(int(pre_element))  # 單純的單音符

                new_note.quarterLength = duration  # 賦予音符長度
                new_note.offset = offset  # 賦予音符在樂曲中的時間軸位置
                midi_notes.append(new_note)

            offset += duration
            pre_element = element
            duration = 0.25  # 基本單位設為 1/4 拍（十六分音符）
        else:
            duration += 0.25  # 若遇到延音符 '-'，將當前音符長度拉長 1/4 拍

    # --- 第二部分：解碼伴奏和弦 (Chords) ---
    duration = 0.0
    offset = 0.0
    for element in chords:
        if element != "-":
            if pre_element != None:
                if pre_element == "0":
                    new_note = note.Rest()
                elif pre_element.startswith("["):
                    # 與音符處同理的字串清單解析
                    a = list(pre_element)
                    c = list(pre_element)
                    for i in range(0, len(a)):
                        if (
                            a[i] == "["
                            or a[i] == ","
                            or a[i] == "]"
                            or a[i] == " "
                        ):
                            c.remove(a[i])
                        elif a[i + 1].isdigit():
                            t = a[i] + a[i + 1]
                            c.remove(a[i])
                            c.remove(a[i + 1])
                            c.insert(i, t)
                    b = list(map(int, c))
                    b = list(set(b))
                    new_note = chord.Chord(b)
                else:
                    new_note = note.Note(int(pre_element))

                new_note.quarterLength = duration
                new_note.offset = offset
                midi_chords.append(new_note)

            offset += duration
            pre_element = element
            duration = 0.25
        else:
            duration += 0.25

    # --- 第三部分：設定樂器音色與寫入檔案 ---
    if ins == "piano":
        i, i2 = instrument.Piano(), instrument.Piano()
    elif ins == "guitar":
        i, i2 = instrument.Guitar(), instrument.Guitar()
    elif ins == "saxphone":
        i, i2 = instrument.Saxphone(), instrument.Saxphone()
    elif ins == "trumpet":
        i, i2 = instrument.Trumpet(), instrument.Trumpet()

    # 建立音樂總譜串流，並分為雙軌（軌道 1 放音符，軌道 2 放和弦）
    score_stream = stream.Stream()
    p1 = stream.Part(midi_notes)
    p2 = stream.Part(midi_chords)

    score_stream.insert(0, p1)
    score_stream.insert(1, p2)
    p1.insert(0, i)  # 注入主旋律樂器
    p2.insert(0, i2)  # 注入伴奏樂器

    # 寫入 BPM 樂曲速度
    score_stream.insert([0, tempo.MetronomeMark(number=bpm)])
    score_stream.insert([1, tempo.MetronomeMark(number=bpm)])

    # 輸出寫入成實體 .mid 檔案
    score_stream.write("mid", fp=midi_path)


def generator(Note_model, Chord_model, ins, bpm, emotion, a):
    """音樂生成器主控排程函數。

    設定全域對應表、呼叫 RNN 模型生成序列，並呼叫解碼轉檔。
    """
    global note2int, int2note, chord2int, int2chord

    # 如果輸入資料夾有現成音樂，就以它為基底發展（續寫）；沒有就從頭盲創
    if os.listdir(INPUTS_PATH):
        data, filenames = encode_data(INPUTS_PATH)
    else:
        data, filenames = from_scratch(emotion)

    # 載入該情緒與子參數對應的字典對照表
    note2int = NOTE_TO_INT(emotion, a)
    int2note = INT_TO_NOTE(emotion, a)
    chord2int = CHORD_TO_INT(emotion, a)
    int2chord = INT_TO_CHORD(emotion, a)

    # 1. 生成音符序列
    notes = generate_notes(Note_model, data, emotion, filenames, a)

    # 2. 生成和弦序列
    chords, midipath = generate_chord(Chord_model, data, emotion, filenames, a)

    # 3. 把序列結合成 MIDI 檔
    convert_midi(notes, chords, midipath, ins, bpm)

    # 4. 調用外部工具，把 MIDI 電子樂譜渲染成實體音訊 Wave 檔案
    convert_wav(midipath, filenames, emotion)


if __name__ == "__main__":
    # 測試執行：載入正向/積極（positive）情緒的音符與和弦權重模型
    Note_model = build_Note_model(
        emotion="positive", weights_path="weights/positive/Note_weights0.hdf5"
    )
    Chord_model = build_Chord_model(
        emotion="positive", weights_path="weights/positive/Chord_weights0.hdf5"
    )

    # 啟動生成器：使用鋼琴音色、速度 120 BPM、正面情緒、子參數帶入 0
    generator(Note_model, Chord_model, "piano", 120, "positive", 0)
