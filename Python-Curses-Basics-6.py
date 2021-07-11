# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:07:47 2021

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
    
    screen.addstr(0, 0, "Name of terminal : " + str(curses.termname()))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(1, 0, "Output of curses.termattrs() : " + str(curses.termattrs()))
    screen.refresh()
    curses.napms(3000)
    
    capname = 'colors'
    screen.addstr(2, 0, "Output of curses.tigetflag(colors) : " + str(curses.tigetflag(capname)))
    screen.addstr(3, 0, "Output of curses.tigetnum(colors) : " + str(curses.tigetnum(capname)))
    screen.addstr(4, 0, "Output of curses.tigetstr(colors) : " + str(curses.tigetstr(capname)))
    screen.refresh()
    curses.napms(5000)
    
    screen.addstr(6, 0, "screen.encoding : " + str(screen.encoding))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(7, 0, "screen.getparyx()" + str(screen.getparyx()))
    # output will be (-1, -1) since there is no parent window for this screen
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(8, 0, "Adding new line at 4, 0")
    screen.refresh()
    curses.napms(3000)
    screen.move(4, 0)
    screen.insertln()
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(10, 0, "Adding 3 new lines before 2, 0")
    screen.refresh()
    curses.napms(3000)
    screen.move(2, 0)
    screen.insdelln(3)
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(16, 0, "screen.is_wintouched() : " + str(screen.is_wintouched()))
    screen.refresh()
    curses.napms(3000)
    
    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> curses.termname()
        -> curses.termattrs()
        -> curses.tigetflag()
        -> curses.tigetnum()
        -> curses.tigetstr()
        -> screen.is_wintouched()
        -> screen.insdelln()
        -> screen.insertln()
        -> screen.getparyx()
        -> screen.encoding
        -> screen.move()
        -> screen.addstr()
        -> screen.refresh()
        -> curses.initscr()
        -> curses.napms()
        -> curses.endwin()

Link for output

"""