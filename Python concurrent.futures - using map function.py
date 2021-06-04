# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:47:44 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

 Caesar's cipher shifts each letter by a number of letters. If the shift 
 takes you past the end of the alphabet, just rotate back to the front of
 the alphabet. In the case of a rotation by 3, w, x, y and z would map to z,
 a, b and c.

In this article, I will show the usage of executor.map for more than one argument being passed
to the designated function.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""


import concurrent.futures
import string
import random


def caesar_cipher(inp_str, change):
    answer = ""

    for i in inp_str:
        if 97 <= ord(i) <= 122:
            asc = ord(i) + change
            while asc > 122:
                asc = 97 + asc - 122 - 1
            answer = answer + chr(asc)
        elif 65 <= ord(i) <= 90:
            asc = ord(i) + change
            while asc > 90:
                asc = 65 + asc - 90 - 1
            answer = answer + chr(asc)
        else:
            answer = answer + i
    
    return answer


def take_input():
    print("Menu")
    print("1. Give input")
    print("2. Generate Random Input")
    choice = int(input("Enter Choice : "))
    inps = []
    changes = []
    
    if choice == 1:
        num = int(input("Enter number of string you would like to enter : "))
        print("Enter input in format : {string change}")
        for i in range(num):
            print("Enter set {}".format(i))
            s, c = map(str, input().split())
            c = int(c)
            inps.append(s)
            changes.append(c)
    else:
        num = random.randint(2, 10)
        for i in range(num):
            n = random.randint(3, 8)
            res = ''.join(random.choices(string.ascii_lowercase, k=n))
            inps.append(res)
            changes.append(n)
    
    return inps, changes


if __name__ == "__main__":    
    inps, changes = take_input()
    with concurrent.futures.ProcessPoolExecutor() as ppe:
        for string, cc in zip(zip(inps, changes), ppe.map(caesar_cipher, inps, changes)):
            print("String [{}] is encoded to [{}] with change [{}]".format(string[0], cc, string[1]))
    

"""
Explanation:
    caesar_cipher: We iterate through the characters of the string and we first add the
    change value to the ascii value of the letter being iterated, we then check if it
    still lies in the ascii range of alphabets(small or capital), if it doesn't then we 
    come back to the beginning letter(a/A) and add the difference. This has been done for
    both capital and small letter.
    
    take_input: We give the user a choice to either give in their input or we generate a random
    input for the same.
    
    main: we use a ProcessPoolExecutor as the executor, we can also use ThreadPoolExecutor.
    we then send the input strings and change values in seperate lists through the map 
    function. we zip all values in order to print them easily.
    
Short Explanation:
    We are taking input of the string and change for the respective string. We then use a
    ProcessPoolExecutor and map the output of the string after caesar cipher encoding is
    applied.
"""