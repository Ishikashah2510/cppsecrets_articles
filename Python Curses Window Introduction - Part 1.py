# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:16:54 2021

@author: Ishika
"""


"""
Window objects, as returned by initscr() and newwin(), have the following methods and attributes:
    
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.


In this article, I will be introducing the window part of the curses module.

The first step would be to install curses module.
cmd command : 
    pip install windows-curses
    
Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

detail_dict = {'window.addch(y, x, ch[,attr])': 'Paint character ch at (y, x) with attributes attr',
               'window.addnstr(y, x, str[,attr])': 'Paint at most n characters of the character string str at (y, x)',
               'window.addstr(y, x, str[,attr])': 'Paint the character string str at (y, x) with attributes attr',
               'window.attroff(attr)': 'Remove attribute attr from the “background” set applied to all writes to the current window.',
               'window.attron(attr)': 'Add attribute attr from the “background” set applied to all writes to the current window.',
               'window.attrset(attr)': 'Set the “background” set of attributes to attr.',
               'window.bkgd(ch[,attr])': 'Set the background property of the window to the character ch, with attributes attr.',
               'window.bkgdset(ch[,attr])': 'Set the window’s background. ',
               'window.border()': 'Draw a border around the edges of the window',
               'window.box()': 'Similar to border(), but both ls and rs are vertch and both ts and bs are horch. ',
               'window.chgat(varying set of attributes)': 'Set the attributes of num characters at the current cursor position, or at position (y, x) if supplied.',
               'window.clear()': 'Like erase(), but also cause the whole window to be repainted upon next call to refresh().',
               'window.clearok(flag)': 'If flag is True, the next call to refresh() will clear the window completely.',
               'window.clrtobot()': 'Erase from cursor to the end of the window',
               'window.clrtoeol()': 'Erase from cursor to the end of the line.',
               'window.cursyncup()': 'Update the current cursor position of all the ancestors of the window',
               'window.delch([y, x])': 'Delete any character at (y, x)',
               'window.deleteln()': 'Delete the line under the cursor',
               'window.derwin(varying set of attributes)': 'An abbreviation for “derive window”',
               'window.echochar()': 'Add character ch with attribute attr',
               'window.enclose(y,x)': 'Test whether the given pair of screen-relative character-cell coordinates are enclosed by the given window',
               'window.encoding()': 'Encoding used to encode method arguments',
               'window.erase()': 'Clear the window',
               'window.getbegyx()': 'Return a tuple (y, x) of co-ordinates of upper-left corner.',
               'window.getbkgd()': 'Return the given window’s current background character',
               'window.getch()': 'Get a character.',
               'window.get_wch()': 'Get a wide character.',
               'window.getkey()': 'Get a character, returning a string instead of an integer, as getch() does',
               'window.getmaxyx()': 'Return a tuple (y, x) of the height and width of the window.',
               'window.getparyx()': 'Return the beginning coordinates of this window relative to its parent window as a tuple (y, x)',}

def blue_print(text):
    return '\033[34m' + text + '\033[00m'

def purple_print(text):
    return '\033[35m' + text + '\033[00m'

for key, val in detail_dict.items():
    print(blue_print(key) + ' : ' + purple_print(val))

print(len(detail_dict.items()))