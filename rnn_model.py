from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
from keras import Model
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils.np_utils import to_categorical
from encoding_module import *
from utils import *
import tensorflow as tf


def create_training_Note_data(corpus_path,emotion,a,segment_length=SEGMENT_LENGTH):
    """Creates training data for the RNN model.

    :param segment_length (int): Length of each segment we want to divide the encoded data into
    :param corpus_path (str): Path to the corpus

    :return input_notes (ndarray): Input part of training data
    :return output_notes (ndarray): Output part of training data
    """

    # load corpus
    with open(corpus_path, "rb") as filepath:
        corpus = pickle.load(filepath)

    # input and output of training data
    input_notes = []
    output_notes = []

    # get the index of filler
    filler_index = NOTE_TO_INT(emotion,a)['*']

    # process each song in the corpus
    for song in corpus:

        # append fillers to the song 
        song = [filler_index]*segment_length + song + [filler_index]
        
        # create segment-target pairs
        for i in range(len(song)-segment_length):
                
            segment = song[i: i+segment_length]
            target = song[i+segment_length]

            input_notes.append(segment)
            output_notes.append(target)

    # one-hot vectorize input and output
    input_notes = to_categorical(input_notes, num_classes=len(NOTE_TO_INT(emotion,a)))
    output_notes = to_categorical(output_notes, num_classes=len(NOTE_TO_INT(emotion,a)))

    return input_notes, output_notes

def create_training_Chord_data(corpus_path,emotion,a,segment_length=SEGMENT_LENGTH):
    """Creates training data for the RNN model.

    :param segment_length (int): Length of each segment we want to divide the encoded data into
    :param corpus_path (str): Path to the corpus

    :return input_notes (ndarray): Input part of training data
    :return output_notes (ndarray): Output part of training data
    """

    # load corpus
    with open(corpus_path, "rb") as filepath:
        corpus = pickle.load(filepath)

    # input and output of training data
    input_notes = []
    output_notes = []

    # get the index of filler
    filler_index = CHORD_TO_INT(emotion,a)['*']

    # process each song in the corpus
    for song in corpus:

        # append fillers to the song 
        song = [filler_index]*segment_length + song + [filler_index]
        
        # create segment-target pairs
        for i in range(len(song)-segment_length):
                
            segment = song[i: i+segment_length]
            target = song[i+segment_length]

            input_notes.append(segment)
            output_notes.append(target)

    # one-hot vectorize input and output
    input_notes = to_categorical(input_notes, num_classes=len(CHORD_TO_INT(emotion,a)))
    output_notes = to_categorical(output_notes, num_classes=len(CHORD_TO_INT(emotion,a)))

    return input_notes, output_notes

def build_Note_model(emotion,a,weights_path=None):
    """Builds RNN model.

    :param weights_path (str): Path to weights of RNN model

    :return model: RNN model
    """

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE, return_sequences=True),
                            input_shape=(SEGMENT_LENGTH, len(NOTE_TO_INT(emotion,a)))))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE)))
    model.add(tf.keras.layers.Dense(units=len(NOTE_TO_INT(emotion,a))))
    
    model.add(tf.keras.layers.Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    # summarise model or load weights
    if weights_path==None:

        model.summary()

    else:

        model.load_weights(weights_path)

    return model

def build_Chord_model(emotion,a,weights_path=None):
    """Builds RNN model.

    :param weights_path (str): Path to weights of RNN model

    :return model: RNN model
    """

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE, return_sequences=True),
                            input_shape=(SEGMENT_LENGTH, len(CHORD_TO_INT(emotion,a)))))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=RNN_SIZE)))
    model.add(tf.keras.layers.Dense(units=len(CHORD_TO_INT(emotion,a))))
    
    model.add(tf.keras.layers.Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    # summarise model or load weights
    if weights_path==None:

        model.summary()

    else:

        model.load_weights(weights_path)

    return model


def train_note_model(input_notes, output_notes, weights_path,emotion,a):
    """Trains and saves RNN model.

    :param input_notes (ndarray): Input part of training data
    :param output_notes (ndarray): Output part of training data
    :param weights_path (str): Path to weights of RNN model

    :return:
    """

    # build RNN model
    model = build_Note_model(emotion,a)

    # load weights or delete it
    if os.path.exists(weights_path):
        
        try:

            model.load_weights(weights_path)
            print("checkpoint loaded")
        
        except:

            os.remove(weights_path)
            print("checkpoint deleted")

    print("Train on %d samples" %(input_notes.shape[0]))

    # save weights
    checkpoint = ModelCheckpoint(filepath=weights_path,
                                 monitor='loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='min')

    # train model
    model.fit(x=input_notes,
              y=output_notes,
              batch_size=BATCH_SIZE,
              epochs=EPOCHS,
              callbacks=[checkpoint])
    

def train_Chord_model(input_notes, output_notes, weights_path,emotion,a):
    """Trains and saves RNN model.

    :param input_notes (ndarray): Input part of training data
    :param output_notes (ndarray): Output part of training data
    :param weights_path (str): Path to weights of RNN model

    :return:
    """

    # build RNN model
    model = build_Chord_model(emotion,a)

    # load weights or delete it
    if os.path.exists(weights_path):
        
        try:

            model.load_weights(weights_path)
            print("checkpoint loaded")
        
        except:

            os.remove(weights_path)
            print("checkpoint deleted")

    print("Train on %d samples" %(input_notes.shape[0]))

    # save weights
    checkpoint = ModelCheckpoint(filepath=weights_path,
                                 monitor='loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='min')

    # train model
    model.fit(x=input_notes,
              y=output_notes,
              batch_size=BATCH_SIZE,
              epochs=EPOCHS,
              callbacks=[checkpoint])
    
def training_model(x,weight,emotion):
    
    input_notes, output_notes = create_training_Note_data(CORPUS_PATH+emotion+'/Note_corpus_'+str(x)+'.bin',emotion,x)
    train_note_model(input_notes, output_notes,weight+'/Note_weights'+str(x)+'.hdf5',emotion,x)
    input_notes, output_notes = create_training_Chord_data(Chord_CORPUS_PATH+emotion+'/Chord_corpus_'+str(x)+'.bin',emotion,x)
    train_Chord_model(input_notes, output_notes,weight+'/Chord_weights'+str(x)+'.hdf5',emotion,x)



if __name__ == "__main__":
    training_model()
    