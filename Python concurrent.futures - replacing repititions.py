# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:12:05 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, we will replace repititions of a character as a star(*) while using
ThreadPoolExecutor to show the working along with command line input

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import concurrent.futures

def star_replace(q):
    q = list(q)
    for ch in range(len(q)):
        for c in range(ch+1, len(q)):
            if q[ch] == q[c] and q[ch] != " ":
                q[c] = '*'
            else:
                continue
    
    out = "".join(q)
    return out


def color_print(string, choice=1):
    if choice == 0:
        return "\033[92m" + str(string) + "\033[0m"
    elif choice == 1:
        return "\u001b[36;1m" + str(string) + "\033[0m"


if __name__ == "__main__":
    test_cases = int(input("Number of strings you would like to enter : "))
    for i in range(test_cases):
        string = input(color_print("Enter the string : ", 0))
        string = [string]
        # print(string)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for string, res in zip(string, executor.map(star_replace, string)):
                print(color_print(string) + " becomes " + color_print(res))


"""
Explanation:
    star_replace: We iterate through a string's characters and convert repititive
    characters into stars. We do not include space character as a repitition. This can be
    used as a form of encoding.
    color_print: We print in color using this function.
    main: Here we first input number of test cases, and then take the input string, and
    use a ThreadPoolExecutor to get the result.
"""