# -*- coding: utf-8 -*-

"""
Created on Mon Jun 14 14:40:40 2021

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

detail_dict = {'curses.resize_term(nlines, ncols)': 'Backend function of resizeterm',
               'curses.resizeterm(nlines, ncols)': 'To resize terminal to specified size',
               'curses.savetty': 'To save the current state of terminal modes',
               'curses.get_escdelay': 'To fetch the escdelay value',
               'curses.set_escdelay(ms)': 'To set the escdelay value',
               'curses.get_tabsize()': 'to get the tab size',
               'curses.set_tabsize(size)': 'To set the tab size',
               'curses.setsyx(y, x)': 'Set cursor to y, x',
               'curses.setupterm(term=None, fd=-1)': 'To initialize the terminal',
               'curses.start_color()': 'To intialize the basic 8 colors',
               'curses.termattrs()': 'Return a logical OR of all video attributes supported by the terminal.',
               'curses.termname()': 'Return the value of the environment variable TERM, as a bytes object',
               'curses.tigetflag(capnum)': 'Return the value of the Boolean capability corresponding to the terminfo capability name capname as an integer',
               'curses.tigetnum(capnum)': 'Return the value of the numeric capability corresponding to the terminfo capability name capname as an integer',
               'curses.tigetstr(capnum)': 'Return the value of the string capability corresponding to the terminfo capability name capname as an integer',
               'curses.tparm(str)': 'Instantiate the bytes object str with the supplied parameters',
               'curses.typeahead(fd)': 'Specify that the file descriptor fd be used for typeahead checking',
               'curses.unctrl(ch)': 'Return a bytes object which is a printable representation of the character ch',
               'curses.ungetch(ch)': 'Push ch so the next getch() will return it.',
               'curses.update_lines_cols()': 'Update LINES and COLS. Useful for detecting manual screen resize.',
               'curses.unget_wch(ch)': 'Push ch so the next get_wch() will return it.',
               'curses.ungetmouse(id, x, y, z, bstate)': 'Push a KEY_MOUSE event onto the input queue',
               'curses.use_env(flag)': 'When flag is False, the values of lines and columns specified in the terminfo database will\n be used, even if environment variables LINES and COLUMNS (used by default) are set',
               'curses.use_default_colors()': 'Allow use of default values for colors on terminals supporting this feature',
               'curses.wrapper(func, /)': 'Initialize curses and call another callable object, func',}

def blue_print(text):
    return '\033[34m' + text + '\033[00m'

def purple_print(text):
    return '\033[35m' + text + '\033[00m'

for key, val in detail_dict.items():
    print(blue_print(key) + ' : ' + purple_print(val))
