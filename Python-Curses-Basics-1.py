# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:36:24 2021

@author: Ishika
"""


"""
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.


In this article, I will be introducing the basic functions of curses module.

The first step would be to install curses module.
cmd command : 
    pip install windows-curses


It is recommended to run this code file in the command prompt by using 'python filename.py' command.

Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

import curses

if __name__ == "__main__":
    screen = curses.initscr()
    
    curses.beep()
    
    curses.napms(3000)
    
    curses.flash()
    
    curses.napms(2000)
    
    screen.addstr(0, 0, 'Hello there, I am at (0,0) position')
    screen.addstr(1, 2, 'I am at (1,2) position')
    
    screen.refresh()
    
    curses.napms(4000)
    
    screen.addstr(5, 5, "I will be going in 2 seconds")
    
    screen.refresh()
    
    curses.napms(2000)
    
    screen.clear()
    
    curses.napms(2000)
    
    screen.addstr(0, 0, "This is a fresh screen")
    
    screen.refresh()
    
    screen.addstr(1, 0, "Can change color : " + str(curses.can_change_color()))
    screen.addstr(2, 0, "has color : " + str(curses.has_colors()))
    
    screen.refresh()
    
    print("I am printed before the screen closes")
    
    curses.napms(3000)
    
    curses.endwin()
    
    print("Thank you!")


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> curses.initscr()
        -> curses.napms(ms)
        -> curses.beep()
        -> curses.flash()
        -> curses.endwin()
        -> window.addstr(position_x, position_y, string)
        -> window.refresh()
        -> window.clear()
        -> curses.can_change_color()
        -> curses.has_colors()

Link for output
https://youtu.be/V3rJmKA4ah0 
"""