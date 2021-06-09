# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:26:24 2021

@author: Ishika
"""


"""
About WAV format:
    Waveform Audio File Format (WAVE, or WAV due to its filename extension; pronounced "wave") is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs.

WAVE module:
    The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.


In this article, I will be introducing the write wav file part of the wave module.

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
import pyaudio

chunk = 1024

sample_format = pyaudio.paInt16
channels = 1

sample_rate = 16000
seconds = 10


def color_print(string):
    return "\u001b[33;1m" + str(string) + "\033[0m"


def record_audio():
    pa = pyaudio.PyAudio()

    stream = pa.open(format=sample_format, channels=channels,
                     rate=sample_rate, input=True,
                     frames_per_buffer=chunk)

    print("Recording started")

    frames = []

    for j in range(0, int(sample_rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)


    stream.stop_stream()
    stream.close()


    pa.terminate()

    print('Done')
    return pa, frames


def open_wave(filename):
    wav_obj = wave.open(filename, 'wb')
    print("opening : ", color_print(filename + 'in write mode'))
    return wav_obj


def wav_file_save(wave_write, pa, frames):
    wave_write.setnchannels(channels)
    wave_write.setsampwidth(pa.get_sample_size(sample_format))
    wave_write.setframerate(sample_rate)
    wave_write.writeframes(b''.join(frames))
    wave_write.close()
    print(color_print("File/Audio saved"))


def file_info(wav_obj):
    print("Number of channels : ", color_print(wav_obj.getnchannels()))
    print("Sample width in bytes : ", color_print(wav_obj.getsampwidth()))
    print("Frame rate : ", color_print(wav_obj.getframerate()))
    print("Number of audio frames : ", color_print(wav_obj.getnframes()))
    print("Parameters : ", color_print(wav_obj.getparams()))
    return wav_obj


if __name__ == '__main__':
    pa, frames = record_audio()
    filename = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/sample_save.wav'
    wave_write = open_wave(filename)
    wav_file_save(wave_write, pa, frames)
    wave_read = wave.open(filename, 'rb')
    print("opening : ", color_print(filename + 'in read mode'))
    file_info(wave_read)
    


"""
Explanation:
    We have used pyAudio module to record audios, which we are then saving using wave module.
    
    color_print: prints given text in color
    record_audio: uses pyAudio to record a audio file
    open_wave: opens wave file in write mode
    wav_file_save: saving wave file with set parameters
    file_info: reading information about file to make sure it is saved as expected


As discussed here, this article shows the implementation of wav_write objects.

https://cppsecrets.com/users/13355105115104105107971051151041175048484864103109971051084699111109/Python-wave-introduction.php

"""