# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:02:25 2021

@author: Ishika
"""


"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

In this article, I will show how to implement a basic counter to count capital and
small letters and space alongwith the vocabulary- count using _thread module.

Function definitions:
    counter: Responsible for reading the file and counting required parameters
    main: starts a thread to call the function counter

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread


def counter():
    path = "D:/codes/python_codes/cppsecrets_internship_may-july-2021/poem.txt"
    f = open(path, "r")
    caps = 0; small = 0; space = 0; vowel_words = 0
    lines = []
    for line in f:
        lines.append(line[:-1])
        for ch in line:
            if 'A' <= ch <= 'Z':
                caps += 1
            elif 'a' <= ch <= 'z':
                small += 1
            elif ch == ' ':
                space += 1
    print("Capitals are ", caps)
    print("small are ", small)
    print("Spaces are ", space)
    
    words = []
    word_co = {}
    
    for l in lines:
        words = l.split()
        for i in words:
            if i[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel_words += 1
            if i not in word_co.keys():
                word_co[i] = 1
            else:
                word_co[i] += 1
    
    print(word_co)
    print("No. of words starting with vowels are ", vowel_words)


if __name__ == "__main__":
    _thread.start_new_thread(counter, ())
    _thread.exit()


"""
Explanation:
    We first count the number of capital, small letters along with the spaces and
    then we count the number of words starting with vowels.
"""