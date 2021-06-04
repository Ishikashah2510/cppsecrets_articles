# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:17:02 2021

@author: Ishika
"""


"""
Running several threads is similar to running several different programs concurrently, but with the following benefits −
Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.
It can be pre-empted (interrupted).
It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.
There are two different kind of threads −
kernel thread
user thread
Kernel Threads are a part of the operating system, while the User-space threads are not implemented in the kernel.

In this article, I will show the basic use of _thread module.

Function definition:
    print_string: This function is responsible for putting  athread to sleep for
    'delay' seconds and print string whenever the thread wakes up.
    print_passed_string: This function is responsible solely for printing a passed string

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

# importing necessary libraries

import _thread, time


def print_passed_string(string):
    print(string)


def print_string(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % (threadName, "Hello, Now I am running"))


if __name__ == '__main__':
    try:
       _thread.start_new_thread(print_string, ("Thread-1", 2, ))
       _thread.start_new_thread(print_string, ("Thread-2", 4, ))
    except:
       print ("Error: unable to start thread")

    try:
        pass_string = "This was a passed string"
        _thread.start_new_thread(print_passed_string, (pass_string, ))
    except:
        print("Error: Not able to start thread")


"""
Explaination of Code:
    First we import the necessary libraries with import _thread, time
    
    print_passed_string: printing argument passed
    
    print_string function: we set count to 0 initially, until count reaches 5
    we put the thread to sleep for 'delay' seconds. Then we print the thread name
    and some string.
    
    main function: we try to start 2 threads namely Thread-1, Thread-2 with delay
    set to 2 and 4 seconds respectively. Next, we start another thread to print a 
    passed string.
    
Observation

The thread with print_passed_string as the is called later but prints first, as
the other threads are sleeping for 2 and 4 seconds.
"""