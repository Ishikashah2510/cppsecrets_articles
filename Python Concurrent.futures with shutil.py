# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:41:37 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, I will show how to use shutil commands with threadpoolexecuter.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

from concurrent.futures import ThreadPoolExecutor
import shutil
import random
from pathlib import Path
import string

path = 'D:/codes/python_codes/cppsecrets_internship_may-july-2021/'


def file_create(x):
    file = open(path + 'file' + str(x) + '.txt', 'w')
    n = random.randint(10, 30)
    res = ''.join(random.choices(string.ascii_uppercase, k=n))
    file.write(res)


def copy_shutil():
    with ThreadPoolExecutor(max_workers=4) as e:
        for i in range(4):
            e.submit(shutil.copy,
                     path + 'file' + str(i) + '.txt',
                     path + 'dest' + str(i) + '.txt')
            print("Copied {} as {}".format('file' + str(i) + '.txt',
                                           'dest' + str(i) + '.txt'))


def move_shutil():
    with ThreadPoolExecutor(max_workers=4) as e:
        dest_path = "D:/codes/python_codes/"
        for i in range(4):
            e.submit(shutil.move,
                     path + 'dest' + str(i) + '.txt',
                     dest_path + 'dest' + str(i) + '.txt')
            print("Moved {} to {}".format(path + 'dest' + str(i) + '.txt',
                                          dest_path + 'dest' + str(i) + '.txt'))
if __name__ == "__main__":
    for i in range(4):
        file_create(i)
    copy_shutil()
    move_shutil()


"""
Explanation:
    We use ThreadPoolExecuter to copy 4 files into the same destination. 
    Next, we shift the 4 files to a different location.
"""