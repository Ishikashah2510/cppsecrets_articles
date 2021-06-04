# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:58:03 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.


In this article, I will show how to implement a simple calculator with each thread
calling a different function

Function definitions:
    number_generator: This function is responsible for generating two random numbers.
    add: This function is responsible for adding two given numbers.
    sub: This function is responsible for subtracting two given numbers.
    multiply: This function is responsible for multiplying two given numbers. 
    raiseto: This function is responsible for raising one number to another.
    divide: This function is responsible for dividing one number by another.
    menu: This function is responsible for starting a thread based on the random
    choice.
    main: This function is responsible for calling menu function.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread
import random
import time
import sys


def number_generator():
    a = random.randint(20, 80)
    b = random.randint(50, 100)
    
    print("\nThe two numbers generated are : {} and {}".format(a, b))
    # time.sleep(5)
    return a, b


def add(n1, n2):
    print("The sum of {} and {} is : {}".format(n1, n2, n1+n2))
    # time.sleep(5)


def sub(n1, n2):
    print("{} subtracted from {} is {}".format(n1, n2, n2-n1))
    print("{} subtracted from {} is {}".format(n2, n1, n1-n2))
    # time.sleep(5)


def multiply(n1, n2):
    print("{} multiplied by {} is {}".format(n1, n2, n1*n2))
    # time.sleep(5)


def raiseto(n1, n2):
    print("{} raised to {} is {}".format(n1, n2, n1**n2))
    print("{} raised to {} is {}".format(n2, n1, n2**n1))
    # time.sleep(5)


def divide(n1, n2):
    try:
        print("{} divided by {} is {}".format(n1, n2, n1/n2))
    except:
        print("The denominator is zero, hence cannot divide")
    try:
        print("{} divided by {} is {}".format(n2, n1, n2/n1))
    except:
        print("The denominator is zero, hence cannot divide")
    # time.sleep(5)


def menu():
    print("Menu")
    print("1. Add two random numbers")
    print("2. Subtract two random numbers from each other")
    print("3. Multiply two random numbers")
    print("4. Raise two random numbers to each other")
    print("5. Divide two random numbers by each other")
    print("0. Exit")
    
    for i in range(5):
        choice  = random.randint(1, 5)
        print("-"*50)
        print("\nRandom choice made : ", choice)
        n1, n2 = number_generator()
        print()
        if choice == 1:
            _thread.start_new_thread(add, (n1, n2))
        elif choice == 2:
            _thread.start_new_thread(sub, (n1, n2))
        elif choice == 3:
            _thread.start_new_thread(multiply, (n1, n2))
        elif choice == 4:
            _thread.start_new_thread(raiseto, (n1, n2))
        elif choice == 5:
            _thread.start_new_thread(divide, (n1, n2))
        time.sleep(2)
    choice = 0
    if choice == 0:
        sys.exit()


if __name__ == "__main__":
    menu()
    print("Bye!")


"""
Explanation:
    number_generator: We generated two random numbers, printed them and returned them
    to the calling function.
    
    add: we add the two numbers and print the result
    
    sub: we subtract both numbers from each other and print the result.
    
    multiply: we multiply the two numbers and print the result.
    
    raiseto: we raise the two numbers to each other and print the result.
    
    divide: we divide the two numbers by each other and print the result.
    
    menu: we generate a random choice from 1 to 5 and start a thread based on the choice.
    
    main: we call menu function to start.
    
Observation: 
    Each thread starts, implements it's assigned function in the order desired.
"""