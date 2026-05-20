import datetime
import numpy as np
from music21 import stream
from music21 import chord,instrument,tempo
from rnn_model import *
from midi2audio import FluidSynth
from song import convert_wav

import shutil


def from_scratch(emotion,midi_num=MIDI_NUM):
    """Creates empty encoded songs for generating music from scratch.

    :param midi_num (int): Number of MIDI files
    
    :return data (list): Empty initial music sequences
    :return filenames (list): Filenames generated based on the date time
    """

    # encoded songs and their file names
    data = []
    filenames = []

    # read current time
    nowTime = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M')
    for midi_index in range(midi_num):

        data.append([])
        filenames.append(emotion+nowTime+'-'+str(midi_index+1))
    # create empty data with names


    
    return data, filenames


def sample(prediction, temperature=TEMPERATURE):
    """Sampling the probability vector output by RNN model.

    :param prediction (ndarray): Probability vector output by RNN model
    :param temperature (float): 0 is equivalent to argmax/max and inf is equivalent to uniform sampling
    
    :return index (int): Index of the sampled result
    """

    # change the distribution of probability
    prediction = np.log(prediction) / temperature
    probabilites = np.exp(prediction) / np.sum(np.exp(prediction))

    # random sampling
    index = np.random.choice(range(len(probabilites)), p=probabilites)

    return index


def generate_notes(model, data,emotion, filenames,a, max_notes=MAX_BARS):
    """Generates notes with RNN model.

    :param model: RNN model
    :param data (list): Encoded songs
    :param filenames (list): File names of the encoded songs
    :param max_notes (int): Maximum number of notes to be generated
    
    :return:
    """

    # process each song in data
    for index in range(len(data)):
        
        # append fillers to the song 
        song = ['*']*SEGMENT_LENGTH + data[index]

        # map each element in the song to int
        try:

            input_notes = [note2int[note] for note in song[-SEGMENT_LENGTH:]]

        except:

            print("Warning: Unknown notes found in \"%s\"" %filenames[index])
            continue
        
        midi_path = OUTPUTS_PATH+ '\\' + filenames[index] + '.mid'
        print("Processing \"%s\"" %midi_path)

        output_note = None
        num_notes = 0
        n=0
        # generate note if no '*' is sampled or the number of notes does not exceed the limit
        while (num_notes<max_notes or max_notes==0) and output_note!='*':
            
            # one-hot vectorize input and add an axis to it
            one_hot_input = to_categorical(input_notes, num_classes=len(NOTE_TO_INT(emotion,a)))
            one_hot_input = one_hot_input[np.newaxis, ...]

            # predict the next note
            prediction = model.predict(one_hot_input)[0]
            note_index = sample(prediction)
            output_note = int2note[note_index]
            print(output_note)
            # update the input sequence
            input_notes = input_notes[1:]
            input_notes.append(note_index)
            
            num_notes += 1
            if output_note!='*':
                song.append(output_note)
        # convert_midi(song[SEGMENT_LENGTH:], midi_path)
        return song[SEGMENT_LENGTH:]


def generate_chord(model, data,emotion, filenames,a, max_notes=MAX_BARS):
    """Generates notes with RNN model.

    :param model: RNN model
    :param data (list): Encoded songs
    :param filenames (list): File names of the encoded songs
    :param max_notes (int): Maximum number of notes to be generated
    
    :return:
    """

    # process each song in data
    for index in range(len(data)):
        
        # append fillers to the song 
        song = ['*']*SEGMENT_LENGTH + data[index]

        # map each element in the song to int
        try:

            input_notes = [chord2int[note] for note in song[-SEGMENT_LENGTH:]]

        except:

            print("Warning: Unknown notes found in \"%s\"" %filenames[index])
            continue
        
        midi_path = OUTPUTS_PATH+ '\\' + filenames[index] + '.mid'
        print("Processing \"%s\"" %midi_path)

        output_note = None
        num_notes = 0
        n=0
        # generate note if no '*' is sampled or the number of notes does not exceed the limit
        while (num_notes<max_notes or max_notes==0) and output_note!='*':
            
            # one-hot vectorize input and add an axis to it
            one_hot_input = to_categorical(input_notes, num_classes=len(CHORD_TO_INT(emotion,a)))
            one_hot_input = one_hot_input[np.newaxis, ...]

            # predict the next note
            prediction = model.predict(one_hot_input)[0]
            note_index = sample(prediction)
            output_note = int2chord[note_index]
            print(output_note)
            # update the input sequence
            input_notes = input_notes[1:]
            input_notes.append(note_index)
            
            num_notes += 1
            if output_note!='*':
                song.append(output_note)
        # convert_midi(song[SEGMENT_LENGTH:], midi_path)
        return song[SEGMENT_LENGTH:],midi_path

def convert_midi(notes,chords, midi_path,ins,bpm):
    """Converts the encoded song to a midi file.

    :param song (list): Encoded song
    :param midi_path (str): Path to the midi file
    
    :return:
    """

    # initialization
    midi_notes = []
    midi_chords = []
    pre_element = None
    duration = 0.0
    offset = 0.0
    a = [0,4,7]
    # decode the song
    for element in notes:
        
        if element!='-':

            # create new note
            if pre_element!=None:
                if pre_element=='0':

                    new_note = note.Rest()
                
                elif pre_element.startswith('['):
                    a=list(pre_element)
                    c=list(pre_element)
                    for i in range(0,len(a)):
                        
                        if a[i] == '[' or a[i] == ',' or a[i]==']' or a[i] ==' ':
                            c.remove(a[i])
                            
                        elif a[i+1].isdigit():
                            t = a[i]+a[i+1]
                            c.remove(a[i])
                            c.remove(a[i+1])
                            c.insert(i, t)
                            
                    
                    b = list(map(int,c))
                    b = list(set(b))
                    new_note = chord.Chord(b)
                    
                else:
                    new_note = note.Note(int(pre_element))

                new_note.quarterLength = duration
                new_note.offset = offset
                midi_notes.append(new_note)
            
            # update offset and save current note
            offset += duration
            pre_element = element
            duration = 0.25
        
        else:
            
            # update duration
            duration += 0.25
    duration = 0.0
    offset = 0.0
    for element in chords:
        
        if element!='-' :

            # create new note
            if pre_element!=None:
                if pre_element=='0':

                    new_note = note.Rest()
                
                elif pre_element.startswith('['):
                    a=list(pre_element)
                    c=list(pre_element)
                    print(str(a))
                    for i in range(0,len(a)):
                        
                        if a[i] == '[' or a[i] == ',' or a[i]==']' or a[i] ==' ':
                            c.remove(a[i])
                            
                        elif a[i+1].isdigit():
                            t = a[i]+a[i+1]
                            c.remove(a[i])
                            c.remove(a[i+1])
                            c.insert(i, t)
                            
                    
                    b = list(map(int,c))
                    b = list(set(b))
                    print(str(b))
                    new_note = chord.Chord(b)
                    print(new_note)
                else:
                    new_note = note.Note(int(pre_element))

                new_note.quarterLength = duration
                new_note.offset = offset
                midi_chords.append(new_note)
            
            # update offset and save current note
            offset += duration
            pre_element = element
            duration = 0.25
        
        else:
            
            # update duration
            duration += 0.25
    # save as midi
    if ins == 'piano':
        i = instrument.Piano()#樂器變數
        i2 = instrument.Piano()
    elif ins == 'guitar':
        i = instrument.Guitar()#樂器變數
        i2 = instrument.Guitar()
    elif ins == 'saxphone':
        i = instrument.Saxphone()#樂器變數
        i2 = instrument.Saxphone()
    elif ins == 'trumpet':
        i = instrument.Trumpet()#樂器變數
        i2 = instrument.Trumpet()
    
    score_stream = stream.Stream()
    p1 = stream.Part(midi_notes)
    p2 = stream.Part(midi_chords)
    score_stream.insert(0,p1)
    score_stream.insert(1,p2)
    p1.insert(0,i)
    p2.insert(0,i2)
    score_stream.insert([0, tempo.MetronomeMark(number=bpm)])
    score_stream.insert([1, tempo.MetronomeMark(number=bpm)])#BPM樂曲拍速
    score_stream.write('mid', fp=midi_path)
        

    


def generator(Note_model,Chord_model,ins,bpm,emotion,a):
    global note2int,int2note,chord2int,int2chord
    if os.listdir(INPUTS_PATH):

        data, filenames = encode_data(INPUTS_PATH)
    else:

        data, filenames = from_scratch(emotion)
    note2int = NOTE_TO_INT(emotion,a)
    int2note = INT_TO_NOTE(emotion,a)
    chord2int = CHORD_TO_INT(emotion,a)
    int2chord = INT_TO_CHORD(emotion,a)


    
    notes = generate_notes(Note_model, data,emotion, filenames,a)
    
    
    
    chords,midipath = generate_chord(Chord_model, data,emotion, filenames,a)
    convert_midi(notes,chords,midipath,ins,bpm)
    convert_wav(midipath,filenames,emotion)



if __name__ == "__main__":

    # generate music from scratch or based on existing file
    # if os.listdir(INPUTS_PATH):

    #     data, filenames = encode_data(INPUTS_PATH)
    # else:

    #     data, filenames = from_scratch()
    Note_model = build_Note_model(emotion='positive',weights_path='weights/positive/Note_weights'+str(0)+'.hdf5')
    Chord_model = build_Chord_model(emotion='positive',weights_path='weights/positive/Chord_weights'+str(0)+'.hdf5')
    generator(Note_model,Chord_model,'piano',120,'positive')
    # convert_wav('midi_output/Sweden2.mid','Sweden2.mid')