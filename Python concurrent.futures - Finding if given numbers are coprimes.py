# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:11:29 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

A Co-prime number is a set of numbers or integers which have only 1 as their common factor i.e. their highest common factor (HCF) will be 1. Co-prime numbers are also known as relatively prime or mutually prime numbers. It is important that there should be two numbers in order to form co-primes.

In this article, we will find if two given numbers are co primes or not

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import math
import concurrent.futures
import random


def check_co_prime(num1, num2):
    if num1 is 0 and num2 is 0:
        return "Invalid numbers"
    elif math.gcd(num1,num2) is 1:
        return "Co-primes"
    else:
        return "Not co primes"


def color_print(p_inp):
    return "\033[95m" + str(p_inp) + "\033[00m"

if __name__ == "__main__":
    nums1 = []
    nums2 = []
    for i in range(5):
        nums1.append(random.randint(1, 10))
        nums2.append(random.randint(20, 30))
    
    with concurrent.futures.ProcessPoolExecutor() as ppe:
        for nums, res in zip(zip(nums1, nums2), ppe.map(check_co_prime, nums1, nums2)):
            print(color_print(nums[0]) + " and " + color_print(nums[1]), end=" ")
            print("are " + color_print(res))


"""
Explanation:
    check_co_prime: This function states that if both the numbers are 0, then the given
    numbers are invalid. If the GCD(Greatest Common Divisor) is 1 then the two numbers are
    coprimes else they are termed as not coprimes.
    
    color_print: This function is responsible for printing in color, the color we have
    used here is pink.
    
    main: This function generats 5 sets of numbers randomly and uses ProcessPoolExecutor
    and map to map the results with the respective set of numbers considered.

"""
    