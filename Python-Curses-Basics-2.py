# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:54:49 2021

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
    
    screen.border(0)
    screen.hline(2, 2, '-', 50)
    
    screen.refresh()
    
    y, x = screen.getyx()
    
    string = 'Hello there, This is a string typing a character one at a time'
    
    y += 1
    x += 1
    
    for c in string:
        screen.addch(y, x, c)
        screen.refresh()
        curses.napms(50)
        x += 1
    
    curses.napms(100)
    
    screen.addstr(y+1, 2, "A verticle line will appear starting from (3, 4) for length 7")
    screen.refresh()
    
    curses.napms(1000)
    
    screen.vline(3, 4, '+', 7)
    screen.refresh()
    
    curses.napms(1000)
    
    screen.addstr(9, 4, 'The baudrate of the terminal is : ' + str(curses.baudrate()))
    screen.refresh()
    
    curses.napms(1000)
    
    screen.clear()
    
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)
    
    for i in range(0, 255):
        screen.addstr(str(i) + " ", curses.color_pair(i))
    screen.refresh()
    
    curses.napms(3000)

    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> window.border()
        -> window.hline()
        -> window.getyx()
        -> window.addch()
        -> window.vline()
        -> window.refresh()
        -> curses.baudrate()
        -> curses.start_color()
        -> curses.use_default_colors()
        -> curses.init_pair()
        -> curses.color_pair()
        -> curses.initscr()
        -> curses.napms(ms)
        -> curses.endwin()

Link for output
https://youtu.be/_iFknolImJA
"""