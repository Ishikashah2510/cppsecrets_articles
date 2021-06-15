# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:43:12 2021

@author: Ishika
"""

"""
About WAV format:
    Waveform Audio File Format (WAVE, or WAV due to its filename extension; pronounced "wave") is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs.

WAVE module:
    The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.


In this article, I will be showing how to read all wav files whose names are mentioned in a csv file.

The first step would be to install wave module.
cmd command : 
    pip install wave
Anaconda cmd command:
    conda install wave
Jupyter notebook command:
    ! pip install wave


We used pandas to read the csv file and then wave to open each file in read format.
    
Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""


import wave
import pandas as pd


def color_print(string):
    return "\u001b[33;1m" + str(string) + "\033[0m"


def read_from_csv(csv_path):
    all_wav_objs = []
    
    data = pd.read_csv(csv_path, header=0)
    
    for i in range(len(data)):
        path = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/'
        wav_read = wave.open(path + data.iloc[i][0], 'rb')
        all_wav_objs.append(wav_read)
        print("Finished reading ", color_print(data.iloc[i][0]))
    
    return all_wav_objs


def file_info(wav_obj):
    print("Number of channels : ", color_print(wav_obj.getnchannels()))
    print("Sample width in bytes : ", color_print(wav_obj.getsampwidth()))
    print("Frame rate : ", color_print(wav_obj.getframerate()))
    print("Number of audio frames : ", color_print(wav_obj.getnframes()))
    print("Parameters : ", color_print(wav_obj.getparams()))
    
    return


if __name__ == "__main__":
    csv_path = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/wave_file_data.csv'
    all_wav = read_from_csv(csv_path)
    for i in all_wav:
        file_info(i)

