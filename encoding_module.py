import json
import os
import pickle

from music21 import chord, converter, instrument, interval, key, note, pitch
from utils import *


def transpose(score):
    """將樂譜自動移調至「C大調」或「A小調」，以統一數據分佈，降低模型的學習難度。

    :param score: 原始的 music21 樂譜物件
    :return score: 移調後的樂譜物件
    """
    for element in score.recurse():
        # 尋找樂譜中的調號（Key Signature）
        if isinstance(element, key.Key):
            # 如果是大調，找出其主音（Tonic）
            if element.mode == "major":
                tonic = element.tonic
            # 如果是小調，找出其關係大調的主音
            else:
                tonic = element.parallel.tonic

            # 計算當前主音與目標「C音」之間的音程差距（Gap）
            gap = interval.Interval(tonic, pitch.Pitch("C"))
            # 將整份樂譜依照差距進行移調
            score = score.transpose(gap)
            break

        # 如果在遇到調號之前就先遇到了音符或休止符，代表此檔案可能沒寫調號，直接中斷
        elif (
            isinstance(element, note.Note)
            or isinstance(element, note.Rest)
            or isinstance(element, chord.Chord)
        ):
            break
        else:
            continue

    return score


def encode_note_data(dataset_path):
    """遍歷資料夾，讀取音樂檔案，並將其中的旋律「音符」與「休止符」編碼為文字序列。

    :param dataset_path (str): 存放原始 MIDI/MusicXML 檔案的資料夾路徑
    :return data, filenames (list): 編碼後的歌曲序列清單、對應的檔案名稱清單
    """
    data = []
    filenames = []

    # 使用 os.walk 遞迴遍歷資料夾內的所有檔案
    for dirpath, dirlist, filelist in os.walk(dataset_path):
        for this_file in filelist:
            # 檢查副檔名是否在允許的清單中（例如 .mid, .midi）
            if os.path.splitext(this_file)[-1] not in EXTENSION:
                continue

            filename = os.path.join(dirpath, this_file)

            try:
                # 解析音樂檔案
                score = converter.parse(filename)
            except:
                print('Warning: Failed to read "%s"' % filename)
                continue

            print('Parsing "%s"' % filename)

            # 通常預設抽取第一個軌道（Part 0）作為主要旋律線，並將結構拍平（flat）
            score = score.parts[0].flat

            # （原程式將此行註解了，若要啟用自動移調可打開）
            # score = transpose(score)

            song = []

            # 遍歷軌道中的每一個音樂元素
            for element in score.recurse():
                # 情況 A：如果是單音符
                if isinstance(element, note.Note):
                    note_pitch = element.pitch.midi  # 轉換成標準 MIDI 數字代碼 (如 60 代表中央C)
                    note_duration = element.quarterLength  # 取得音符時值（以四分音符為單位，1.0 代表一拍）

                # 情況 B：如果是休止符
                elif isinstance(element, note.Rest):
                    note_pitch = 0  # 用 0 代表休止符
                    note_duration = element.quarterLength

                # 情況 C：如果是和弦（在旋律音符模式下，只取和弦的最高音）
                elif isinstance(element, chord.Chord):
                    note_pitch = element.notes[-1].pitch.midi
                    note_duration = element.quarterLength

                else:
                    continue

                # 檢查音符的長度是否為 0.25 拍（十六分音符）的整數倍，用以規範節奏時間軸
                if int(note_duration % 0.25) == 0:
                    # 注意：此處原程式寫死每次都補兩個 '-'，這會固定音符生成的間隔
                    song += [str(note_pitch)] + ["-"] * 2
                else:
                    # 如果出現怪異的節奏（如三連音或無法整除的長度），拋出警告並捨棄這首歌
                    print(note_duration)
                    song = None
                    print(
                        'Warning: Found an unacceptable duration when reading the file "%s"'
                        % filename
                    )
                    break

            # 如果歌曲編碼成功，將其收入結果陣列
            if song != None:
                data.append(song)
                filenames.append(
                    os.path.splitext(os.path.basename(filename))[0]
                )

    print("Successfully encoded %d songs" % (len(data)))
    return data, filenames


def encode_Chord_data(dataset_path):
    """遍歷資料夾，將音樂檔案中的「和弦伴奏」單獨提取出來進行文字序列編碼。"""
    data = []
    filenames = []

    for dirpath, dirlist, filelist in os.walk(dataset_path):
        for this_file in filelist:
            if os.path.splitext(this_file)[-1] not in EXTENSION:
                continue

            filename = os.path.join(dirpath, this_file)

            try:
                score = converter.parse(filename)
            except:
                print('Warning: Failed to read "%s"' % filename)
                continue

            print('Parsing "%s"' % filename)
            score = score.parts[0].flat
            song = []

            for element in score.recurse():
                # 在和弦資料庫中，我們「只」處理 music21 的 Chord 物件，忽略單音與休止符
                if isinstance(element, chord.Chord):
                    # 印出該和弦包含的所有 MIDI 音高數字組合
                    a = [p.midi for p in element.pitches]
                    print(a)

                    # 這裡使用 normalOrder（標準排列音程組合，例如 C和弦 C-E-G 會轉為 [0, 4, 7]）
                    note_pitch = element.normalOrder
                    note_duration = element.quarterLength
                else:
                    continue

                # 檢查時值合規性
                if int(note_duration % 0.25) == 0:
                    # 儲存和弦標籤，後面補上 8 個延音符 '-'
                    song += [str(note_pitch)] + ["-"] * 8
                else:
                    print(note_duration)
                    song = None
                    print(
                        'Warning: Found an unacceptable duration when reading the file "%s"'
                        % filename
                    )
                    break

            if song != None:
                data.append(song)
                filenames.append(
                    os.path.splitext(os.path.basename(filename))[0]
                )

    print("Successfully encoded %d songs" % (len(data)))
    return data, filenames


def save_Note_corpus(
    data, emotion, corpus_path=CORPUS_PATH, vocabulary_path=VOCABULARY_PATH
):
    """建立音符的字典檔 (.json) 與語料庫代碼檔 (.bin)。"""
    a = 0
    # 1. 蒐集所有歌曲中出現過的所有不重複符號，並手動加入特殊填充符 '*'，進行排序
    vocabulary = sorted(set(sum(data, []) + ["*"]))

    # 2. 自動尋找尚未被佔用的編號（如從 0 到 999），避免覆蓋之前的成果
    for i in range(1000):
        if os.path.exists(
            vocabulary_path + emotion + "/Note_voca_" + str(i) + ".json"
        ):
            i += 1
        else:
            a = i
            # 將字典清單儲存為 scannable 的 JSON 檔案
            with open(
                vocabulary_path + emotion + "/Note_voca_" + str(a) + ".json",
                "w",
            ) as filepath:
                json.dump(vocabulary, filepath, indent=4)
            break

    # 3. 呼叫外部函數讀取剛建好的字典，將歌曲中的「文字符號」轉換為「整數索引（Index）」
    note2int = NOTE_TO_INT(emotion, a)
    corpus = [[note2int[note] for note in song] for song in data]

    # 4. 同理，以不覆蓋舊檔為原則，將整數化的語料庫序列打包成二進位二級制檔案（pickle）
    for i in range(1000):
        if os.path.exists(
            corpus_path + emotion + "/Note_corpus_" + str(i) + ".bin"
        ):
            i += 1
        else:
            with open(
                corpus_path + emotion + "/Note_corpus_" + str(a) + ".bin", "wb"
            ) as filepath:
                pickle.dump(corpus, filepath)
            break


def save_Chord_corpus(
    data,
    emotion,
    corpus_path=Chord_CORPUS_PATH,
    vocabulary_path=Chord_VOCABULARY_PATH,
):
    #建立和弦的字典檔 (.json) 與語料庫代碼檔 (.bin)。
    a = 0
    vocabulary = sorted(set(sum(data, []) + ["*"]))

    for i in range(1000):
       
        if os.path.exists(
            vocabulary_path + emotion + "/Chord_voca_" + str(i) + ".json"
        ):
            i += 1
        else:
            a = i
            with open(
                vocabulary_path + emotion + "/Chord_voca_" + str(a) + ".json",
                "w",
            ) as filepath:
                json.dump(vocabulary, filepath, indent=4)
            break

    note2int = CHORD_TO_INT(emotion, a)
    corpus = [[note2int[note] for note in song] for song in data]

    for i in range(1000):
        if os.path.exists(
            corpus_path + emotion + "/Chord_corpus_" + str(i) + ".bin"
        ):
            i += 1
        else:
            with open(
                corpus_path + emotion + "/Chord_corpus_" + str(a) + ".bin", "wb"
            ) as filepath:
                pickle.dump(corpus, filepath)
            break


def encoding_song(path, emotion):
    """核心排程執行項：傳入原生音樂資料夾路徑與情緒標籤，一鍵完成音符與和弦的雙重處理。"""
    # 處理旋律線音符
    note_data, filenames = encode_note_data(path)
    save_Note_corpus(note_data, emotion)

    # 處理伴奏和弦
    chord_data, filenames = encode_chord_data(path)
    save_Chord_corpus(chord_data, emotion)


if __name__ == "__main__":
    # 注意：這裡直接呼叫會報錯，因為 encoding_song 預期要傳入 path 和 emotion 參數
    # 例如：encoding_song('./my_midi_dataset', 'positive')
    encoding_song()
