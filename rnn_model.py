import os
import pickle
import tensorflow as tf
from keras import Model
from keras.layers import Dense, Input, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint

from tensorflow.keras.utils import to_categorical
# 自訂模組，包含音符對應字典與全域變數
from encoding_module import *
from utils import *


def create_training_Note_data(
    corpus_path, emotion, a, segment_length=SEGMENT_LENGTH
):
    """將音符語料庫資料轉換為 RNN 模型訓練所需的輸入與輸出配對。

    :param corpus_path (str): 語料庫（pickle 檔案）的路徑
    :param emotion (str): 情緒標籤，用於對應不同的音符字典
    :param a (int/str): 子參數，用於自訂字典函數
    :param segment_length (int): 預測所需的特徵歷史長度（時間步數）

    :return input_notes (ndarray): 模型輸入（One-hot 編碼後的片段矩陣）
    :return output_notes (ndarray): 模型輸出（One-hot 編碼後的目標標籤）
    """
    # 讀取二進位格式的音符語料庫（包含多首歌曲的音符序列）
    with open(corpus_path, "rb") as filepath:
        corpus = pickle.load(filepath)

    input_notes = []
    output_notes = []

    # 取得用來填補邊界的「填充符號（filler）'*'」在字典中的整數索引
    filler_index = NOTE_TO_INT(emotion, a)["*"]

    # 逐一處理語料庫中的每首歌曲
    for song in corpus:
        # 在歌曲開頭填補 segment_length 個填充符，結尾補一個，確保每首歌曲的第一個音也能被預測
        song = [filler_index] * segment_length + song + [filler_index]

        # 使用滑動視窗（Sliding Window）建立「特徵-標籤」配對
        for i in range(len(song) - segment_length):
            segment = song[i : i + segment_length]  # 輸入：過去的連續音符片段
            target = song[i + segment_length]  # 標籤：緊接著的下一個音符

            input_notes.append(segment)
            output_notes.append(target)

    # 將整數序列轉換為 One-hot 向量，類別總數為音符字典的長度
    num_classes = len(NOTE_TO_INT(emotion, a))
    input_notes = to_categorical(input_notes, num_classes=num_classes)
    output_notes = to_categorical(output_notes, num_classes=num_classes)

    return input_notes, output_notes


def create_training_Chord_data(
    corpus_path, emotion, a, segment_length=SEGMENT_LENGTH
):
    """將和弦語料庫資料轉換為 RNN 模型訓練所需的輸入與輸出配對（邏輯與音符版本完全相同）。"""
    with open(corpus_path, "rb") as filepath:
        corpus = pickle.load(filepath)

    input_notes = []
    output_notes = []

    # 取得和弦字典中的填充符號整數索引
    filler_index = CHORD_TO_INT(emotion, a)["*"]

    for song in corpus:
        song = [filler_index] * segment_length + song + [filler_index]

        for i in range(len(song) - segment_length):
            segment = song[i : i + segment_length]
            target = song[i + segment_length]

            input_notes.append(segment)
            output_notes.append(target)

    # 轉換為和弦的 One-hot 編碼
    num_classes = len(CHORD_TO_INT(emotion, a))
    input_notes = to_categorical(input_notes, num_classes=num_classes)
    output_notes = to_categorical(output_notes, num_classes=num_classes)

    return input_notes, output_notes


def build_Note_model(emotion, a, weights_path=None):
    """建構並編譯預測音符的雙向 LSTM 模型。

    :param emotion (str): 情緒標籤
    :param a (int/str): 子參數
    :param weights_path (str): 選擇性提供已儲存的模型權重路徑
    :return model: 編譯完成的 Keras 模型
    """
    vocab_size = len(NOTE_TO_INT(emotion, a))

    model = tf.keras.models.Sequential()

    # 第一層：雙向 LSTM，return_sequences=True 代表會輸出每個時間步的精神狀態，供下一層 LSTM 使用
    model.add(
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(units=RNN_SIZE, return_sequences=True),
            input_shape=(SEGMENT_LENGTH, vocab_size),
        )
    )

    # 第二層：雙向 LSTM，只輸出最後一個時間步的結果（壓縮成單一向量）
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE)))

    # 全連接層，將維度映射到所有可能的音符總數
    model.add(tf.keras.layers.Dense(units=vocab_size))

    # 激活函數層：使用 Softmax 計算出預測每個音符的機率分佈
    model.add(tf.keras.layers.Activation("softmax"))

    # 編譯模型：多元分類使用 categorical_crossentropy，優化器為 rmsprop（常應用於 RNN）
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    # 如果沒有指定權重，就印出結構圖；有指定就載入舊權重
    if weights_path is None:
        model.summary()
    else:
        model.load_weights(weights_path)

    return model


def build_Chord_model(emotion, a, weights_path=None):
    """建構並編譯預測和弦的雙向 LSTM 模型（結構與音符模型相同，唯獨輸出層大小對應和弦字典）。"""
    vocab_size = len(CHORD_TO_INT(emotion, a))

    model = tf.keras.models.Sequential()
    model.add(
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(units=RNN_SIZE, return_sequences=True),
            input_shape=(SEGMENT_LENGTH, vocab_size),
        )
    )
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE)))
    model.add(tf.keras.layers.Dense(units=vocab_size))
    model.add(tf.keras.layers.Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    if weights_path is None:
        model.summary()
    else:
        model.load_weights(weights_path)

    return model


def train_note_model(input_notes, output_notes, weights_path, emotion, a):
    """負責執行音符模型的訓練流程與存檔。"""
    # 建立一個全新的音符模型
    model = build_Note_model(emotion, a)

    # 檢查是否有歷史檢查點（權重檔案）。如果有，嘗試載入以繼續訓練；若損壞則刪除。
    if os.path.exists(weights_path):
        try:
            model.load_weights(weights_path)
            print("歷史檢查點載入成功")
        except Exception:
            os.remove(weights_path)
            print("歷史檢查點損壞，已將其刪除並重新訓練")

    print("開始訓練，樣本總數: %d" % (input_notes.shape[0]))

    # 設定 Keras 訓練回呼（Callback）：當訓練損失（loss）創新低時，自動覆蓋保存最佳權重
    checkpoint = ModelCheckpoint(
        filepath=weights_path,
        monitor="loss",
        verbose=0,
        save_best_only=True,
        mode="min",
    )

    # 開始動手訓練模型
    model.fit(
        x=input_notes,
        y=output_notes,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        callbacks=[checkpoint],
    )


def train_Chord_model(input_notes, output_notes, weights_path, emotion, a):
    """負責執行和弦模型的訓練流程與存檔（邏輯同上）。"""
    model = build_Chord_model(emotion, a)

    if os.path.exists(weights_path):
        try:
            model.load_weights(weights_path)
            print("歷史檢查點載入成功")
        except Exception:
            os.remove(weights_path)
            print("歷史檢查點損壞，已將其刪除並重新訓練")

    print("開始訓練，樣本總數: %d" % (input_notes.shape[0]))

    checkpoint = ModelCheckpoint(
        filepath=weights_path,
        monitor="loss",
        verbose=0,
        save_best_only=True,
        mode="min",
    )

    model.fit(
        x=input_notes,
        y=output_notes,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        callbacks=[checkpoint],
    )


def training_model(x, weight, emotion):
    """核心排程函數：統整並依序執行「讀取資料 -> 轉換 -> 訓練音符 -> 訓練和弦」的完整工作流。

    :param x (int/str): 標記編號，用於區分不同的語料庫和權重檔名
    :param weight (str): 權重資料夾的儲存路徑
    :param emotion (str): 當前訓練針對的情緒資料夾名稱
    """
    # 1. 建立音符訓練資料，並啟動音符模型訓練
    note_corpus = CORPUS_PATH + emotion + "/Note_corpus_" + str(x) + ".bin"
    note_weight = weight + "/Note_weights" + str(x) + ".hdf5"
    input_notes, output_notes = create_training_Note_data(
        note_corpus, emotion, x
    )
    train_note_model(input_notes, output_notes, note_weight, emotion, x)

    # 2. 建立和弦訓練資料，並啟動和弦模型訓練
    chord_corpus = (
        Chord_CORPUS_PATH + emotion + "/Chord_corpus_" + str(x) + ".bin"
    )
    chord_weight = weight + "/Chord_weights" + str(x) + ".hdf5"
    input_chords, output_chords = create_training_Chord_data(
        chord_corpus, emotion, x
    )
    train_Chord_model(input_chords, output_chords, chord_weight, emotion, x)


if __name__ == "__main__":
    # 注意：這裡直接執行會噴錯，因為 training_model 預期要傳入 3 個參數 (x, weight, emotion)
    # 例如：training_model(1, './weights', 'happy')
    training_model()
