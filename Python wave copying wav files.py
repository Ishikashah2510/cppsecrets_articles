# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:42:51 2021

@author: Ishika
"""

"""
About WAV format:
    Waveform Audio File Format (WAVE, or WAV due to its filename extension; pronounced "wave") is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs.

WAVE module:
    The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.


In this article, I will be showing how to use wave module to copy a wav file.

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


def read_wav_file_to_copy():
    filename = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/sample.wav'
    wave_read = wave.open(filename, 'rb')
    print("Opening : ", color_print(filename + ' in read mode'))
    return wave_read


def wav_file_to_write():
    filename = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/sample_copy.wav'
    wav_obj = wave.open(filename, 'wb')
    print("opening : ", color_print(filename + ' in write mode'))
    return wav_obj


def copy_file(wav_read, wav_write):
    wav_write.setnchannels(wav_read.getnchannels())
    wav_write.setsampwidth(wav_read.getsampwidth())
    wav_write.setframerate(wav_read.getframerate())
    
    frames = []
    for i in range(wav_read.getnframes()):
        frames.append(wav_read.readframes(i))

    wav_write.writeframes(b''.join(frames))
    wav_write.close()
    
    print(color_print("File/Audio saved"))


if __name__ == "__main__":
    wav_read = read_wav_file_to_copy()
    wav_write = wav_file_to_write()
    copy_file(wav_read, wav_write)


"""
Explanation:
    read_wav_file_to_copy: Opens the file to be read.
    
    wav_file_to_write: Opens file in which the audio has to be written into.
    
    copy_file: Sets parameters of the wav file to be written into by using the wav file from being the frames are being read.

"""