# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:26:01 2021

@author: Ishika
"""

"""
About WAV format:
    Waveform Audio File Format (WAVE, or WAV due to its filename extension; pronounced "wave") is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs.

WAVE module:
    The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.


In this article, I will be introducing the read wav file part of the wave module.

The first step would be to install wave module.
cmd command : 
    pip install wave
Anaconda cmd command:
    conda install wave
Jupyter notebook command:
    ! pip install wave
    
Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""


import wave


def color_print(string):
    return "\u001b[33;1m" + str(string) + "\033[0m"


def read_wav():
    filename = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/sample.wav'
    wave_read = wave.open(filename, 'rb')
    print("Opening : ", color_print(filename))
    return wave_read


def file_info(wav_obj):
    print("Number of channels : ", color_print(wav_obj.getnchannels()))
    print("Sample width in bytes : ", color_print(wav_obj.getsampwidth()))
    print("Frame rate : ", color_print(wav_obj.getframerate()))
    print("Number of audio frames : ", color_print(wav_obj.getnframes()))
    print("Compression Type : ", color_print(wav_obj.getcomptype()))
    print("Compression name : ", color_print(wav_obj.getcompname()))
    print("Parameters : ", color_print(wav_obj.getparams()))
    print("Reading only 100 frames")
    wav_obj.readframes(100)
    print("Current position : ", color_print(wav_obj.tell()))
    print("Rewinding to beginning")
    wav_obj.rewind()
    print("Current position : ", color_print(wav_obj.tell()))
    print("Set position of file pointer at 250")
    wav_obj.setpos(250)
    print("Current position : ", color_print(wav_obj.tell()))
    
    return


if __name__ == '__main__':
    wav_obj = read_wav()
    file_info(wav_obj)


"""
As discussed in the last article, this article shows the implementation of wav_read objects.

https://cppsecrets.com/users/13355105115104105107971051151041175048484864103109971051084699111109/Python-wave-introduction.php
"""
