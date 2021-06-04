# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:12:45 2021

@author: Ishika
"""


"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.


In this article, I will show how to implement a simple stopwatch using
_thread library. We won't be using a thread but instead will be using only the
lock to show the functionality of a lock.

Function definitions:
    start_stopwatch: This function is responsible for starting the stopwatch.
    pause_stopwatch: This function is responsible for stopping the stopwatch.
    stop_stopwatch: This function is responsible for stopping the stopwatch.
    time_convert: This function is responsible for converting the time into
    required format and returning it as a string.
    menu_display: This function is responsible for displaying a simple menu
    main: function is responsible for calling menu display

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread
import time
import sys

lock_sw = _thread.allocate_lock()
start_time = time.time()
stop_time = time.time()
time_elapsed = 0


def start_stopwatch():
    global lock_sw
    global start_time
    
    if lock_sw.locked():
        print("\nSorry cannot start another stopwatch while one is running")
    else:
        start_time = time.time()
        lock_sw.acquire()
        print("\nStop watch started")
    menu_display(value=1)


def pause_stopwatch():
    global time_elapsed
    global start_time
    
    if lock_sw.locked():
        print("\nStopwatch has been paused")
        time_elapsed += time.time() - start_time
        lock_sw.release()
        print("Time elapsed till now : ", time_convert(time_elapsed))
    
    menu_display(value=2)


def stop_stopwatch():
    global lock_sw
    global stop_time
    global start_time
    global time_elapsed
    
    if lock_sw.locked():
        lock_sw.release()
        print("\nThe stopwatch has been stopped")
        stop_time = time.time()
        time_elapsed += stop_time - start_time
        print("Time elapsed : ", time_convert(time_elapsed))
    else:
        print("\nSorry, no stopwatch running")
    
    menu_display()


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return "{0}:{1}:{2}".format(int(hours),int(mins),sec)


def menu_display(value=0):
    print("\nPlease make a choice from the below menu : ")
    print("1. Start stopwatch")
    
    if value == 1:
        print("2. Pause stopwatch")
        print("3. Stop stopwatch")
    elif value == 2:
        print("2. Continue stopwatch")
        print("3. Stop stopwatch")

    print("0. Exit application")
    
    choice = int(input("Your choice : "))
    
    if choice == 1:
        start_stopwatch()
    elif choice == 2:
        if value == 1:
            pause_stopwatch()
        elif value == 2:
            start_stopwatch()
    elif choice == 3:
        stop_stopwatch()
    elif choice == 0:
        print("\nThank you for using stopwatch")
        sys.exit()


if __name__ == '__main__':
    print("Welcome to stopwatch app!")
    menu_display()


"""
Explanation:
    The libraries needed in this script are _thread, datetime, time and sys.
    _thread module is used for the stopwatch lock.
    time module is used for calculating time elapsed during the working of the stopwatch.
    sys module is used for ending the execution.
    
    start_stopwatch: If lock_sw is acquired we display an error message stating another
    stopwatch cannot be started as one is already running. If lock_sw is free, we acquire
    it and the time calculation is started.
    
    pause_stopwatch: If lock_sw is acquired we release the lock and calculate the time
    elapsed until then.
    
    stop_stopwatch: If lock_sw is acquired we release the lock and calculate the 
    total time elapsed. If lock_sw is free we display an error message stating that
    no stopwatch is running and hence none can be stopped.
    
    time_convert: We calculate the minutes, hours and seconds using the seconds that
    are pass and return a string in required format.
    
    menu_display: We display the choices and direct the script to the required course
    of action based on the choice made by the user.
    
Observation:
    If the stopwatch is paused the elapsed time duration is added to the total time
    elapsed.

Alternative that can be made:
    Since _thread module is a module with limited functionality, the threading module
    can be used to implement the stopwatch app.
    
    Class can be used to implement the stopwatch.
    
    Timer can be integrated along with the stopwatch.
"""