# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:56:55 2021

@author: Ishika
"""


"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, we will learn when to use processpoolexecutor and threadpoolexecutor

Now that we have studied about both the Executor classes %u2013 ThreadPoolExecutor and ProcessPoolExecutor, we need to know when to use which executor. We need to choose ProcessPoolExecutor in case of CPU-bound workloads and ThreadPoolExecutor in case of I/O-bound workloads.

If we use ProcessPoolExecutor, then we do not need to worry about GIL because it uses multiprocessing. Moreover, the execution time will be less when compared to ThreadPoolExecution. Consider the following Python script example to understand this.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import time
import concurrent.futures

value = [8000000, 7000000]


def counting(n):
   start = time.time()
   while n > 0:
      n -= 1
   return time.time() - start


def main_ppe():
   print("Using ProcessPoolExecutor")
   start = time.time()
   with concurrent.futures.ProcessPoolExecutor() as executor:
      for number, time_taken in zip(value, executor.map(counting, value)):
         print('Start: {} Time taken: {}'.format(number, time_taken))
   print('Total time taken: {}'.format(time.time() - start))


def main_tpe():
   print("Using ThreadPoolExecutor")
   start = time.time()
   with concurrent.futures.ThreadPoolExecutor() as executor:
      for number, time_taken in zip(value, executor.map(counting, value)):
         print('Start: {} Time taken: {}'.format(number, time_taken))
      print('Total time taken: {}'.format(time.time() - start))
if __name__ == '__main__':
    main_ppe()
    main_tpe()


"""
We are using the same function for both ThreadPool and ProcessPool Executor.
    The counting function counts from the given value to 0.

Observation

ThreadPoolExecutor takes more time than ProcessPoolExecutor. Sometimes there is a minor
    difference while there is also a bigger difference observed.
"""