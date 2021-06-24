# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:01:00 2021

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
    
    screen.addstr(0, 0, 'Terminal has insert and delete char capbility : ' + str(curses.has_ic()))
    screen.addstr(1, 0, 'Terminal has insert and delete line capbility : ' + str(curses.has_il()))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(3, 0, 'Window structure modified : ' + str(curses.is_term_resized(20, 20)))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(4, 0, 'Current Kill character : ' + str(curses.killchar()))
    screen.refresh()
    curses.napms(3000)
    
    curses.start_color()
    screen.addstr(6, 0, 'Pair content for number 5 : ' + str(curses.pair_content(5)))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(8, 0, 'Resizing terminal using resize_term in 2 seconds')
    screen.refresh()
    curses.napms(2000)
    curses.resize_term(40, 40)
    screen.addstr(9, 0, 'Resized')
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(11, 0, 'Resizing terminal using resize_term in 2 seconds')
    screen.refresh()
    curses.napms(2000)
    curses.resize_term(100, 120)
    screen.addstr(12, 0, 'Resized')
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(14, 0, 'Setting y,x to 18, 0')
    screen.refresh()
    curses.napms(3000)
    curses.setsyx(18, 0)
    curses.napms(3000)
    
    screen.addnstr(20, 0, 'Printing only till here, not after that', 23)
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(21, 0, 'moving cursor to 15, 0')
    screen.move(15, 0)
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(15, 0, 'Clearing from here to end of window')
    screen.refresh()
    curses.napms(3000)
    screen.clrtobot()
    screen.refresh()
    curses.napms(3000)
    
    
    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> curses.has_ic()
        -> curses.has_il()
        -> curses.is_term_resized()
        -> curses.killchar()
        -> curses.pair_content()
        -> curses.resize_term()
        -> curses.setsyx()
        -> curses.initscr()
        -> curses.napms()
        -> curses.start_color()
        -> curses.endwin()
        -> screen.addnstr()
        -> screen.move()
        -> screen.clrtobot()
        -> screen.addstr()
        -> screen.refresh()

Link for output
https://youtu.be/1PNC4tSazm8
"""