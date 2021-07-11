# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:44:34 2021

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
    
    curses.def_prog_mode()
    curses.def_shell_mode()
    screen.addstr(0, 0, "Saved the current program and shell mode")
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(1, 0, 'Current mouse events : ' + str(curses.getmouse()))
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(2, 0, 'Setting mouse interval to 2 seconds')
    screen.refresh()
    curses.mouseinterval(2000)
    curses.napms(2000)
    
    screen.addstr(3, 0, 'Making a new pad')
    screen.refresh()
    curses.napms(1000)
    new_pad = curses.newpad(20, 20)
    new_pad.refresh(0, 0, 0, 20, 20, 20)
    new_pad.addstr(0, 0, 'Hello there')
    curses.napms(2000)
    
    screen.addstr(5, 0, 'Making a new window')
    screen.refresh()
    curses.napms(1000)
    new_win = curses.newwin(20, 20, 10, 10)
    new_win.addstr(0, 0, 'Hello there')
    new_win.refresh()
    curses.napms(2000)
    
    new_win.addstr(1, 0, 'Moving this window to 0, 0')
    new_win.refresh()
    curses.napms(1000)
    new_win.mvwin(0, 0)
    new_win.addstr(2, 0, 'Moved')
    new_win.refresh()
    curses.napms(2000)
    
    new_win.addstr(3, 0, 'Overwriting window on top of original window')
    new_win.refresh()
    curses.napms(1000)
    new_win.overwrite(screen)
    new_win.refresh()
    curses.napms(2000)
    
    new_win.addstr(3, 0, 'Overlaying window on top of original window')
    new_win.refresh()
    curses.napms(1000)
    new_win.overlay(screen)
    new_win.refresh()
    curses.napms(2000)
    
    new_win.addstr(6, 0, 'Touching entire window')
    new_win.refresh()
    curses.napms(1000)
    new_win.touchwin()
    curses.napms(2000)
    
    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> curses.def_prog_mode()
        -> curses.def_shell_mode()
        -> curses.getmouse()
        -> curses.mouseinterval()
        -> curses.newpad()
        -> curses.newwin()
        -> screen.mvwin()
        -> screen.overwrite()
        -> screen.overlay()
        -> screen.touchwin()
        -> screen.addstr()
        -> screen.refresh()
        -> curses.initscr()
        -> curses.napms()
        -> curses.endwin()

Link for output

"""