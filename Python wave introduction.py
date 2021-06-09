# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:56:48 2021

@author: Ishika
"""


"""
About WAV format:
    Waveform Audio File Format (WAVE, or WAV due to its filename extension; pronounced "wave") is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs.

WAVE module:
    The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.


In this article, I will be introducing the wave module.

The first step would be to install wave module.
cmd command : 
    pip install wave
Anaconda cmd command:
    conda install wave
Jupyter notebook command:
    ! pip install wave
    
Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

# Looking at wave.open method

# We can open a object of wav file, in either of two modes
# The two modes being read('rb') and write('wb')

# Opening a wav file in rb mode returns a wave_read object
# while opening in wb mode returns a wave_write object
# both wave_read and wave_write have different methods which can be used

# Code snippet for read mode

import wave

read_obj = wave.open('filename.wav', 'rb')

# Code snippet for write mode

import wave

write_obj = wave.open('filename.wav', 'wb')

# It must be duly noted that wave does NOT provide read/write functionality.
# It individually allows reading and writing.
# It is also important to know it is the responsibility of the user to close
# a file object, using wave_obj.close() method.

# A wave_read object is adapted with the following functionalities

"""
wave_read.close()        -> To close the read stream created by wave.
wave_read.getnchannels() -> To know the number of audio channels(1 for mono, 2 for stereo)
wave_read.getsampwidth() -> To know the sample's width in bytes.
wave_read.getframerate() -> To know the frame rate/ sampling frequency.
wave_read.getnframes()   -> To know the number of audio frames.
wave_read.getcomptype()  -> To get the compression type.
wave_read.getcompname()  -> To get the commpression name in human readable format.
wave_read.getparams()    -> This method returns a named tuple with (nchannels, sampwidth, framerate, nframes, comptype, compname)
wave_read.readframes(x)  -> To read x number of frames only.
wave_read.rewind()       -> To rewind the file pointer to the beginning of the audio stream.
wave_read.setpos(pos)    -> Set the file pointer to a particular position.
wave_read.tell()         -> To know the current position of the file pointer.

"""

# A wave_write object is adapted with the following functionalities

"""
wave_write.close()                 -> To close the write stream created by wave.
wave_write.setnchannels(n)         -> To set the number of channels.
wave_write.setsampwidth(n)         -> To set the sample width.
wave_write.setframerate(n)         -> To set the framerate.
wave_write.setnframes(n)           -> To set the number of frames.
wave_write.setcomptype(type, name) -> To set the compression type and name.
wave_write.setparams(tuple)        -> To set the parameters (nchannels, sampwidth, framerate, nframes, comptype, compname).
wave_write.tell()                  -> To know the current position in the file.
wave_write.writeframesraw(data)    -> To write the audio frames in raw format.
wave_write.writeframes(data)       -> To write the audio frames with correct number of nframes.

"""
