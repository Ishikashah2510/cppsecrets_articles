# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:13:09 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, we will transfer a given string of numbers to words while using
ProcessPoolExecutor to show the working along with command line input.

Traslating a given string of numbers to words can be used in audio systems, to read
out a given number.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""



import concurrent.futures


def number_split(inp):
    d = {'1':"one" , '2':"two" , '3':"three" , '4':"four" , '5':"five" , '6':"six" , '7':"seven" , '8':"eight" , '9':"nine" , '0':"zero" , }
    if not inp.isnumeric():
        return "The string entered contains non numeric characters"
    q = list(inp)
    out = ''
    for f in q:
        out += d[f] + " "
    return out


def color_print(string, choice=1):
    if choice == 0:
        return "\u001b[33;1m" + str(string) + "\033[0m"
    elif choice == 1:
        return "\u001b[36;1m" + str(string) + "\033[0m"
    
    
if __name__ == "__main__":
    test_cases = int(input(color_print("Enter number of test cases : ", 0)))
    for i in range(test_cases):
        inp = input(color_print("Enter your number string please : ", 0))
        with concurrent.futures.ProcessPoolExecutor() as ppe:
            inp = [inp]
            for inp, res in zip(inp, ppe.map(number_split, inp)):
                print("Digit to word for " + color_print(inp), end=" ")
                print("is " + color_print(res))


"""
Explanation:
    number_split: We split the number to individual digits and write down its word form.
    We take care to check if a given string contains non-numeric characters.
    color_print: This function is responsible for color printing.
    main: We use a processpoolexecutor and implement the number_split function.
"""