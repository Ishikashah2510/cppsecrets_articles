# -*- coding: utf-8 -*-
"""
Created on Thu May 20 19:41:14 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

To learn about stop and wait protocol visit: https://www.javatpoint.com/stop-and-wait-protocol

In this article, I will show how to implement the stop and wait protocol using
_thread library.

Function definitions:
    sender: This function is meant to carry out operations for a sender thread.
    receiver: This function is responsible for carrying out operations for a receiver thread.
    file_create: This function is responsible for creating a text file with a random string
    which will be considered as the string which the sender will send to the receiver.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread
import random
import string

flag = 1
data = ''
i = 0


def sender(a):
    global flag
    global data
    global i
    file_create()
    while(True):
        if data[i] == '1':
            break
        if flag == 1:
            print("Sending  : ", data[i])
            i += 1
            flag = 0


def receiver(a):
    global flag
    global i

    while(True):
        if flag == 0:
            print("Recieved : ", data[i-1])
            flag = 1
            if data[i] == '1':
                break


def file_create():
    file = open('prac4_input.txt', 'w')
    n = random.randint(10, 20)
    res = ''.join(random.choices(string.ascii_uppercase, k=n))
    res = res + '1'
    file.write(res)
    # print("hi")


if __name__ == '__main__':

    file_create()
    file = open("Prac4_input.txt", "r")
    data = file.readline()
    print("The data is : ", data)
    a = 0
    t1 = _thread.start_new_thread(sender, (a,))
    t2 = _thread.start_new_thread(receiver, (a,))


"""
Explanation : 
    The libraries needed for this implementation are threading, _thread, random,
    string.
    
    First I have defined the global variables which will be useful for all the functions.
    
    class all_not_recieved is a class derived from exception to define an exception where
    all the bytes arent sent to the receiver.
    
    Function:
        sender: Here, we append the data that is being sent. The character
        is sent one by one. The sender waits for the flag to become 1.
        
        receiver: Here, we check if character is received only after the flag becomes
        0. The receiver waits for the flag to become 0.
        
        
        file_create: A random string of capital letters of length between 10-30
        is generated and saved in a text file.
        
        main: We read the input data and allocate a lock and start the sender
        and receiver threads.

    
Observation:
    You can see in the output a sender thread sends a new character only
    after receiver receives the sent character.
"""