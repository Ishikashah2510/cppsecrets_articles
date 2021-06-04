# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:44:41 2021

@author: Ishika
"""

"""
Text to Speech is basically the conversion of a given text to a desired speech, which can vary by language, accent etc. The basic systems include training a model by using text spoken by different humans and using the model to predict for some other given data. While there are many systems available to do the same, Google has released it's own API whose demonstration is done below.

About gTTS: 
    gTTS stands for Google Text to Speech. gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.We use gTTS in our article as below. 
"""


from gtts import gTTS, lang
import os
from playsound import playsound


def convert(inp, i):
    language = 'en'
    audio = gTTS(text=inp, lang=language, slow=False, tld='co.in')
    path = "D:/codes/python_codes/cppsecrets_internship_may-july-2021/"
    filename = "converted_audio_tts{}.mp3".format(i)
    audio.save(path + filename)
    playsound(path + filename)


def take_input(i):
    inp = input("Please enter your text : ")
    convert(inp, i)


if __name__ == "__main__":
    i = 1
    # print(lang.tts_langs())
    while True:
        take_input(i)
        
        choice = input("Would you like to enter different text? Enter Y/y for yes : ")
        i += 1
        if choice.lower() != 'y':
            print("Thank you")
            break


"""
Explanation:
    convert: Sets the language, and initializes the gTTS object. We have then defined the filename and path and we play the sound.
    
    take_input: Takes text input and passes on to convert function
    
    main: We call take_input function until user asks to stop
    
Different Parameters that can be used : 
    We can have text to speech for various languages. The default language is set to 'en' i.e. English. It supports all languages supported by Google Translate.
    
    Code snippet for seeing the languages available:
        print(lang.tts_langs())
    
    Code snippet to set a different language:
        # For Hindi Language
        language = 'hi'
        audio = gTTS(text=inp, lang=language, slow=False)
    
        # For Japanese Language
        language = 'ja'
        audio = gTTS(text=inp, lang=language, slow=False)
    
    We can use different accents as well. To set a different accent we need to use the parameter Top Level Domain(tld). 16 accents are supported by the Google TTS API.
    The available accents can be found here https://www.google.com/supported_domains
    Code snippet for changing the accent:
        # For Australian accent
        audio = gTTS(text=inp, lang=language, slow=False, tld='com.au')
        
        # For Indian accent
        audio = gTTS(text=inp, lang=language, slow=False, tld='co.in')
"""