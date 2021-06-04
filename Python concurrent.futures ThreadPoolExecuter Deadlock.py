# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:46:32 2021

@author: Ishika
"""


"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

Deadlock is a situation that occurs in OS when any process enters a waiting state because another waiting process is holding the demanded resource. Deadlock is a common problem in multi-processing where several processes share a specific type of mutually exclusive resource known as a soft lock or software.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import time
from concurrent.futures import ThreadPoolExecutor

def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


if __name__ == "__main__":
    
    executor = ThreadPoolExecutor(max_workers=2)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)
    
"""
Explanation:
    We are first executing wait_on_b to get a as result, but wait_on_b waits for variable
    b's result. When we run to fetch b, wait_on_a waits for value of a, which is waiting for b.
    Hence, leading to deadlock.
"""