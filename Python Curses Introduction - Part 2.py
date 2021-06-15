# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:40:30 2021

@author: Ishika
"""

"""
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.


In this article, I will be introducing the curses module.

The first step would be to install curses module.
cmd command : 
    pip install windows-curses
    
Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

detail_dict = {'curses.init_pair(pair_number, fg, bg)': 'To change the definition of a given color pair',
               'curses.is_term_resized(nlines, ncols)': 'Returns True is the window structure would be modified, else False',
               'curses.isendwin()' : 'Returns True if endwin is called',
               'curses.keyname(k)' : 'Returns the name of the key numbered k',
               'curses.killchar()' : "Returns the user's current line kill character",
               'curses.longname()' : 'Returns the bytes object containing the terminfo long name field',
               'curses.meta(flag)' : 'If flag set to True, it allows 8-bit characters to be input. If False, it allows 7-bit characters only',
               'curses.mouseinterval(interval)' : 'Set the maximum time in milliseconds that can elapse between press \nand release events in order for them to be recognized as a click, and return the previous interval value',
               'curses.mousemask()' : 'Set the mouse events to be reported, and return a tuple (availmask, oldmask)',
               'curses.napms(ms)' : 'Sleep for ms milliseconds',
               'curses.newpad(nlines, ncols)' : 'Create and return a pointer to a new pad data structure with the given number of lines and columns. Return a pad as a window object.',
               'curses.newwin(nlines, ncols, begin_y, begin_x)' : 'Return a new window, whose left-upper corner is at (begin_y, begin_x), and whose height/width is nlines/ncols.',
               'curses.nl()' : 'Enter newline mode',
               'curses.nocbreak()' : 'To leave cbreak mode',
               'curses.noecho()' : 'To leave echo mode',
               'curses.nonl()' : 'To leave newline mode',
               'curses.noqiflush()' : 'You may want to call noqiflush() in a signal handler if you want output to continue as though the interrupt had not occurred, after the handler exits',
               'curses.noraw()' : 'To leave raw mode',
               'curses.pair_content(pair_number)' : 'Return a tuple (fg, bg) containing the colors for the requested color pair.',
               'curses.pair_number(attr)' : 'Return the number of the color-pair set by the attribute value attr.',
               'curses.putp(string)' : 'the output of putp() always goes to standard output',
               'curses.qiflush([flag])' : 'If flag is False, the effect is the same as calling noqiflush(). \nIf flag is True, or no argument is provided, the queues will be flushed when these control characters are read.',
               'curses.raw()' : 'To enter raw mode',
               'curses.reset_prog_mode()' : 'Resets program mode',
               'curses.reset_shell_mode()' : 'Resets shell mode',
               'curses.resetty()' : 'restore the state of terminal mode',}

def blue_print(text):
    return '\033[34m' + text + '\033[00m'

def purple_print(text):
    return '\033[35m' + text + '\033[00m'

for key, val in detail_dict.items():
    print(blue_print(key) + ' : ' + purple_print(val))
