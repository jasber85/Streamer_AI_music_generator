import json
import os

# paths
DATASET_PATH = "midi_training/" #音樂資料集
CORPUS_PATH = "Note_corpus/" #音符辭典
VOCABULARY_PATH = 'Note_voca/' #音符辭典
Chord_CORPUS_PATH = "Chord_corpus/" #音符辭典
Chord_VOCABULARY_PATH = 'Chord_voca/' #音符辭典
Note_WEIGHTS_PATH = 'Note_weights.hdf5'
Chord_WEIGHTS_PATH = 'Chord_weights.hdf5' #音樂權重
INPUTS_PATH = "inputs" #接續生成樂曲
OUTPUTS_PATH = "midi_output" #輸出樂曲資料夾
AUDIO_OUTPUT_PATH = 'audio_output'

# parameters for encoding_module.py
EXTENSION = ['.musicxml', '.xml', '.mxl', '.midi', '.mid', '.krn']

# parameters for rnn_model.py
SEGMENT_LENGTH = 512
RNN_SIZE = 512
BATCH_SIZE = 64
EPOCHS = 30

# parameters for midi_generator.py
MAX_BARS = 1400
TEMPERATURE = 0.7
MIDI_NUM = 1

def NOTE_TO_INT(emotion,a,vocabulary_path=VOCABULARY_PATH):
    """Loads note2int dictionary.

    :param vocabulary_path (str): Path to vocabulary

    :return note2int (dict): Note-to-int mapping
    """

    if os.path.exists(vocabulary_path+emotion+'/Note_voca_'+str(a)+'.json'):
        with open(vocabulary_path+emotion+'/Note_voca_'+str(a)+'.json', 'r') as filepath:
            vocabulary = json.load(filepath)
        return dict((note, index) for index, note in enumerate(vocabulary))



def INT_TO_NOTE(emotion,a,vocabulary_path=VOCABULARY_PATH):
    """Loads int2note dictionary.
    
    :param vocabulary_path (str): Path to vocabulary

    :return int2note (dict): Int-to-note mapping
    """

    if os.path.exists(vocabulary_path+emotion+'/Note_voca_'+str(a)+'.json'):
        with open(vocabulary_path+emotion+'/Note_voca_'+str(a)+'.json', 'r') as filepath:
            vocabulary = json.load(filepath)
        return dict((index, note) for index, note in enumerate(vocabulary))


    
    
#==================================我是分隔線======================================
def CHORD_TO_INT(emotion,a,vocabulary_path=Chord_VOCABULARY_PATH):
    """Loads note2int dictionary.

    :param vocabulary_path (str): Path to vocabulary

    :return note2int (dict): Note-to-int mapping
    """

    if os.path.exists(vocabulary_path+emotion+'/Chord_voca_'+str(a)+'.json'):
        with open(vocabulary_path+emotion+'/Chord_voca_'+str(a)+'.json', 'r') as filepath:
            vocabulary = json.load(filepath)
        return dict((note, index) for index, note in enumerate(vocabulary))

    
    


def INT_TO_CHORD(emotion,a,vocabulary_path=Chord_VOCABULARY_PATH):
    """Loads int2note dictionary.
    
    :param vocabulary_path (str): Path to vocabulary

    :return int2note (dict): Int-to-note mapping
    """

    if os.path.exists(vocabulary_path+emotion+'/Chord_voca_'+str(a)+'.json'):
        with open(vocabulary_path+emotion+'/Chord_voca_'+str(a)+'.json', 'r') as filepath:
            vocabulary = json.load(filepath)
        return dict((index, note) for index, note in enumerate(vocabulary))

    