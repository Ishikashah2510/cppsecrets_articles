# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:44:16 2021

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
    
    curses.start_color()
    screen.addstr(0, 0, 'curses.has_key(25) : ' + str(curses.has_key(25)))
    screen.addstr(1, 0, 'curses.has_key(69) : ' + str(curses.has_key(69)))
    screen.addstr(2, 0, 'curses.keyname(120) : ' + str(curses.keyname(120)))
    screen.addstr(3, 0, 'curses.longname() : ' + str(curses.longname()))
    screen.addstr(4, 0, 'curses.pair_number(50) : ' + str(curses.pair_number(50)))
    # will display 0 as we haven't used color_pair to set any color pairs
    screen.addstr(5, 0, 'curses.unctrl(s) : ' + str(curses.unctrl('s')))
    # returns bytes type object of character passed
    screen.addstr(6, 0, 'reading a wide character : ')
    screen.refresh()
    wide_char = screen.get_wch()
    screen.addstr(7, 0, 'Char read : ' + str(wide_char))
    screen.refresh()
    
    screen.insnstr(2, 0, 'Inserted here using insnstr', 5)
    screen.refresh()
    curses.napms(200)
    screen.insstr(4, 0, 'Inserted here using insstr')
    screen.refresh()
    curses.napms(200)
    
    screen.addstr(8, 0, 'screen.instr(2, 0) : ' + str(screen.instr(2, 0)))
    screen.refresh()
    screen.addstr(9, 0, 'screen.is_linetouched(6) : ' + str(screen.is_linetouched(6)))
    screen.refresh()
    curses.napms(10000)
    
    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> curses.has_key()
        -> curses.keyname()
        -> curses.longname()
        -> curses.pair_number()
        -> curses.unctrl()
        -> screen.get_wch()
        -> screen.insnstr()
        -> screen.insstr()
        -> screen.instr()
        -> screen.is_linetouched()
        -> screen.addstr()
        -> screen.refresh()
        -> curses.initscr()
        -> curses.napms()
        -> curses.endwin()

Link for output

"""