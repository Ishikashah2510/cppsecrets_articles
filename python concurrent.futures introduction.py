# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:57:52 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""


from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import math


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 2, 12)
        print(future.result())
    
    # The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously. ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock but also means that only picklable objects can be executed and returned.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))