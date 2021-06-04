# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:35:42 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.


In this article, I will show how to implement a simple timer using
_thread library.

Function definitions:
    set_timer: This is a function responsible for setting a timer for x
    number of seconds.
    menu_display: This function is responsible for displaying a simple menu
    main: function is responsible for calling menu display

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import _thread
from datetime import datetime, timedelta
import time
import sys

lock_timer = _thread.allocate_lock()


def set_timer(mins, secs):
    global lock_timer
    
    if lock_timer.locked():
        print("Sorry cannot set another timer while one timer is running")
    else:
        total_secs = mins * 60 + secs
        off_time = datetime.now() + timedelta(minutes=mins, seconds=secs)
        print("The timer will go off at : ", off_time)
        lock_timer.acquire(timeout=total_secs)
        time.sleep(total_secs)
        print("Timer done!")


def menu_display():
    print("Please make a choice from the below menu : ")
    print("1. Set a timer")
    print("0. Exit application")
    
    choice = int(input("Your choice : "))
    
    if choice == 1:
        mins = int(input("Enter number of minutes for the timer : "))
        secs = int(input("Enter number of seconds for the timer : "))
        timer_thread = _thread.start_new_thread(set_timer, (mins, secs,))

    elif choice == 0:
        print("Thank you for using timer")
        sys.exit()


if __name__ == '__main__':
    print("Welcome to timer app!")
    menu_display()


"""
Explanation:
    The libraries needed in this script are _thread, datetime, time and sys.
    _thread module is used for the timer lock and to start a new thread.
    datetime module is used for displaying at what time will the timer go off.
    time module is used for putting the script for x number of seconds.
    sys module is used for ending the execution.
    
    set_timer: We check if the lock_timer is locked, and if so we display an error
    message stating the timer cannot be set. If the lock_timer is not acquired we proceed
    to calculate the time at which the timer will go off and then acquiring lock_timer for
    the calculated number of seconds. We then put the script to sleep for the calculated number
    of seconds and then display that the timer is done.
    
    menu_display: We display the choices and direct the script to the required course
    of action based on the choice made by the user.
    
Observation:
    The "Timer done!" statement is displayed after the timer goes off, until then
    the script is closed.

Alternative that can be made:
    Since _thread module is a module with limited functionality, the threading module
    can be used to implement the timer app.
    
"""