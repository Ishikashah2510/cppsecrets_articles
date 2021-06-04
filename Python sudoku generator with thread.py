# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:06:23 2021

@author: Ishika
"""


"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

Sudoku is a logic-based, combinatorial number-placement puzzle. 
In classic sudoku, the objective is to fill a 9×9 grid with digits 
so that each column, each row, and each of the nine 3×3 subgrids that 
compose the grid contains all of the digits from 1 to 9.

In this article, I will show generate a random sudoku puzzle while using
_thread library.

Function definitions:
    generate_sudoku: responsible for generating a random sudoku
    sudoku_style1_print: prints sudoku in style 1
    sudoku_style2_print: prints sudoku in style 2

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import random
import pandas as pd
import numpy as np
import _thread
import time

lock = _thread.allocate_lock()
all0 = np.zeros(shape=(9, 9), dtype=np.int8)
sudoku = pd.DataFrame(all0,
                      columns=range(1, 10),
                      index=range(1, 10))


def generate_sudoku():
    global lock
    global sudoku
    
    row_order = list(range(1, 10))
    row0 = list(range(1, 10))
    random.shuffle(row_order)
    random.shuffle(row0)
    for i in range(len(row_order)):
        if i == 0:
            sudoku.loc[row_order[i]] = row0
        elif i in [3, 6, 9]:
            row0 = row0[1:] + row0[:1]
            sudoku.loc[row_order[i]] = row0
        else:
            row0 = row0[3:] + row0[:3]
            sudoku.loc[row_order[i]] = row0
    
    lock.release()


def sudoku_style1_print():
    global sudoku
    
    print("Printing sudoku in style 1")
    print("-" * 45)
    for i in range(9):
        print("| ", end="")
        for j in range(1, 10):
            try:
                print(str(sudoku.iloc[i][j]) + " | ", end=" ")
            except:
                print('{}:{}'.format(i, j))
            
        print()
        print("-" * 45)
        

def sudoku_style2_print():
    global sudoku
    
    print("Printing sudoku in style 2")
    print("-" * 49)
    for i in range(9):
        print("|\t", end="")
        for j in range(1, 10):
            try:
                print(str(sudoku.iloc[i][j]), end=" ")
            except:
                print('{}:{}'.format(i, j))
            
            if j in [3, 6, 9]:
                print("\t|\t", end="")
        print()
        if i in [2, 5]:
            print("-" * 49)
    print("-" * 49)
        
    
if __name__ == '__main__':
    
    lock.acquire()
    _thread.start_new_thread(generate_sudoku, ())
    
    while True:
        if not lock.locked():
            _thread.start_new_thread(sudoku_style1_print, ())
            time.sleep(2)
            _thread.start_new_thread(sudoku_style2_print, ())
            break


"""
Explanation:
    In sudoku generator, we generate a random order of rows and one random row.
    For all rows we shift the value by either 3 or 1. Illustration as shown below
    
    We have even randomized the order of the rows in order to avoid it from becoming
    obvious.
    We wait for the sudoku generation to be over before printing the sudoku.
    time.sleep(2) is used to avoid the two printing threads to run simultaneously and
    spoil the order of printing
    We have two printing methods for the sudoku.
    
"""