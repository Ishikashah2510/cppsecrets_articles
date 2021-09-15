# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:17:07 2021

@author: Ishika
"""

import random


# approach 1
if __name__ == '__main__':
    list01 = [0] * random.randint(3, 10)
    list01.extend([1] * random.randint(3, 10))
    random.shuffle(list01)
    print("The generated random list of 0 and 1's is ", *list01, sep=" ")
    size = len(list01)
    
    max_len = -1
    max_sublist = []
    
    for iterator in range(size - 1):
        for in_loop in range(iterator, size):
            sublist = list01[iterator:in_loop]
            if sublist.count(0) == sublist.count(1) and len(sublist) > max_len:
                max_len = len(sublist)
                max_sublist = sublist
    
    print('Maximum size of subarray : {}'.format(max_len))
    print('The subarray is : ', *max_sublist, sep=" ")


# approach 2

if __name__ == '__main__':
    list01 = [0] * random.randint(3, 10)
    list01.extend([1] * random.randint(3, 10))
    random.shuffle(list01)
    print("The generated random list of 0 and 1's is ", *list01, sep=" ")
    dictionary_hashmap = {}
    dictionary_hashmap[0] = -1
    size = 0
    end_ind = -1
    summation = 0
    
    for i in range(len(list01)):
        summation += -1 if (list01[i] == 0) else 1
        if summation in dictionary_hashmap:
            if size < i - dictionary_hashmap.get(summation):
                size = i - dictionary_hashmap.get(summation)
                end_ind = i
        else:
            dictionary_hashmap[summation] = i
    if end_ind != -1:
        print((end_ind - size + 1, end_ind))
    else:
        print("No sublist exists")
 
