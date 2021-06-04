# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:47:42 2021

@author: Ishika
"""


"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

As you know, a magic square is a matrix all of whose row sums, 
column sums and the sums of the two diagonals are the same. (One 
diagonal of a matrix goes from the top left to the bottom right, the 
other diagonal goes from top right to bottom left.) 

In this article, I will by direct computation that a given matrix is a magic square or
not using _thread module to check.

Function definitions:
    input_take: takes input for a nxn array.
    checker: verfies if the array is a magic sqaure or not
    main: starts a thread to call the function input_take then satrt a thread for checker.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread
import numpy as np
import time


use = []


def input_take():
    global use
    
    size = int(input("Enter size of array : "))
    
    for i in range(size):
        print("Enter values for row {0}".format(i+1))
        extra = list(map(int, input().split()))
        use.append(extra)


def checker():
    global use
    
    arr = np.array(use)
    col = np.sum(arr, axis=0)
    row = np.sum(arr, axis=1)
    dia1 = sum(arr[i][i] for i in range(size))
    dia2 = sum(arr[size-i-1][size-i-1] for i in range(size))
    col_max = max(col)
    col_min = min(col)
    row_max = max(row)
    row_min = min(row)
    if dia1 == dia2 == col_max == col_min == row_max == row_min:
        print("It's a Magic Sqaure! :D")
    else:
        print("Sorry, not a magic sqaure! :(")
    

if __name__ == "__main__":
    input_take()
    time.sleep(5)
    _thread.start_new_thread(checker, ())
    _thread.exit()


"""
Explanation:
    We first take the input from the user for a nxn array and then calculate
    the sum of the two main diagonals and the minimum and maximum for the columns
    and rows. If all are found to be equal we declare the matrix to be a magic square.
"""