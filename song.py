# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:34:17 2022

@author: jasbe
"""
import shutil
import datetime
import os
from midi2audio import FluidSynth

def convert_wav(path,filenames,emotion):
    print(path)
    nowTime = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M')
    name = emotion+nowTime+'.wav'
    shutil.copy(str(path), str(filenames))
    print(filenames)
    FluidSynth('FluidR3_GM.sf2').midi_to_audio(str(filenames), name)
    os.remove(str(filenames))
    shutil.move(name,'audio_output')