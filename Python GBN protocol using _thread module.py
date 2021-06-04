# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:47:39 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

To learn about go back n protocol visit: https://www.tutorialspoint.com/a-protocol-using-go-back-n

In this article, I will show how to implement the go back n protocol using
_thread library.

Function definitions:
    sender: This function is meant to carry out operations for a sender thread.
    receiver: This function is responsible for carrying out operations for a receiver thread.
    ack: this function is responsible for sending acknowledgement from receiver to sender thread.
    file_create: This function is responsible for creating a text file with a random string
    which will be considered as the string which the sender will send to the receiver.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import threading
import _thread
import random
import string


received = []
data = []
data_send = ""
window = 5
i = 0
flag = 0
h = 0


class all_not_received(Exception):
    pass


def sender(lock):
    global i
    global data_send
    global flag
    while(True):
        if not lock.locked():
            data_send = data[i: i + window]
            i += window
            if data_send[-1] == "1":
                data_send = data_send[:-1]
            if len(data_send) == 0:
                break
            print("Sending : ", *data_send, sep=" ")
            lock.acquire()
            flag = 0
            if i >= len(data):
                break


def ack(lock):
    global received
    global h
    global i
    global send_data
    try:
        # print("Received : ", "".join(received))
        if "".join(received) != data_send:
            raise all_not_received()
        # print("Send_data : ", data_send)
        print("Acknowledgement for  : ", received[-1])
    except all_not_received:
        if len(received) != 0:
            print("Error at : ", received[-1])
            i -= (len(send_data) - len(received))
        else:
            print("Nothing received")
            i -= window
    finally:
        lock.release()
        h = 1


def receiver(lock):
    global received
    global flag
    global h
    while(True):
        if lock.locked() and flag == 0:
            timer = threading.Timer(0.00000000000000000000000001, ack, args=(lock,))
            h = 0
            received = []
            timer.start()
            for _ in data_send:
                received.append(_)
            flag = 1
            if i >= len(data):
                break
        if h == 1 or len(data_send) == 0:
            timer.cancel()
        if len(data_send) == 0:
            break


def file_create():
    file = open('prac4_input_gbn.txt', 'w')
    n = random.randint(10, 30)
    res = ''.join(random.choices(string.ascii_uppercase, k=n))
    res = res + '1'
    file.write(res)


if __name__ == '__main__':

    file_create()
    file = open("Prac4_input_gbn.txt", "r")
    data = file.readline()
    print("The data is : ", data)
    lock = _thread.allocate_lock()
    t1 = _thread.start_new_thread(sender, (lock,))
    t2 = _thread.start_new_thread(receiver, (lock,))
    

"""
Explanation : 
    The libraries needed for this implementation are threading, _thread, random,
    string.
    
    First I have defined the global variables which will be useful for all the functions.
    
    class all_not_recieved is a class derived from exception to define an exception where
    all the bytes arent sent to the receiver.
    
    Function:
        sender: Here, we append the data that is being sent. The data will be sent in
        predefined window sizes. The sender waits for the lock to be freed before sending
        data of the next window.
        
        receiver: Here we have set a timer for receiving the data in the window. 
        Since the data here is small, I have used a very small amount of value for 
        the time of the timer. The receiver waits for the lock to be acquired.
        
        ack: Here the function determines if the data has been completely received
        or has been lost on the way.
        
        file_create: A random string of capital letters of length between 10-30
        is generated and saved in a text file.
        
        main: We read the input data and allocate a lock and start the sender
        and receiver threads.
    
    Note : We are using threading library only for the timer.
    
Observation:
    You can see in the output sometimes the data is not completely received by the
    receiver and hence the ack function prints nothing received. This shows that if
    the data isn't completely sent the receiver doesn't accept part of the data
    and the entire data has to be re-transmitted.
"""