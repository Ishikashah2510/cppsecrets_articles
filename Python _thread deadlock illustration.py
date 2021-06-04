# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:08:45 2021

@author: Ishika
"""
"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
    

In this article, I will show the basic illustration of deadlock.
There exist many other ways a deadlock can occur but I will be showing 
a very basic example in order to understand easily.

Function definitions:
    time: acquires lock1 first then lock2 and tries to print time
    space: acquires lock2 first then lock1 and tries to print space
    main: starts a new thread for the two functions

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

# deadlock
import _thread

lock1 = _thread.allocate_lock()
lock2 = _thread.allocate_lock()


def time():
    global lock1
    global lock2
    
    while True:
        if not lock1.locked():
            lock1.acquire()
            if not lock2.locked():
                lock2.acquire()
                print("Time")


def space():
    global lock1
    global lock2
    
    while True:
        if not lock2.locked():
            lock2.acquire()
            if not lock1.locked():
                lock1.acquire()
                print("Space")


if __name__ == "__main__":
    thread1 = _thread.start_new_thread(time, ())
    thread2 = _thread.start_new_thread(space, ())


"""
What is happening?
When time thread starts, it acquires lock1 and then lock2, now space thread starts
and it waits for thread1 to release both locks in order to move forward. since we haven't used
release function anywhere or have not set a timeout for acquiring the two locks, the waiting
becomes infinite hence leading to a deadlock.

output: time

output: space
"""

# solution
import _thread

lock1 = _thread.allocate_lock()
lock2 = _thread.allocate_lock()


def time():
    global lock1
    global lock2
    
    while True:
        if not lock1.locked():
            lock1.acquire(timeout=2)
            if not lock2.locked():
                lock2.acquire(timeout=2)
                print("Time")


def space():
    global lock1
    global lock2
    
    while True:
        if not lock2.locked():
            lock2.acquire(timeout=2)
            if not lock1.locked():
                lock1.acquire(timeout=2)
                print("Space")


if __name__ == "__main__":
    thread1 = _thread.start_new_thread(time, ())
    thread2 = _thread.start_new_thread(space, ())


"""
What is happening?
We acquired the locks for only a given time limit, hence giving both threads a chance.

output :time
        space
"""