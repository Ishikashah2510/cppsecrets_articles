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

detail_dict = {'window.getstr(varying set of parameters)': 'Read a bytes object from the user, with primitive line editing capacity.',
               'window.getyx()': 'Return a tuple (y, x) of current cursor position relative to the window’s upper-left corner',
               'window.hline(varying set of parameters)': 'Display a horizontal line starting at (y, x) with length n consisting of the character ch.',
               'window.idcok(flag)': 'If flag is False, curses no longer considers using the hardware insert/delete character feature of the terminal;',
               'window.idlok(flag)': 'If flag is True, curses will try and use hardware line editing facilities.',
               'window.immedok(flag)': 'If flag is True, any change in the window image automatically causes the window to be refreshed',
               'window.inch([y, x])': 'Return the character at the given position in the window.',
               'window.insch(varying set of parameters)': 'Paint character ch at (y, x) with attributes attr',
               'window.insdelln(nlines)': 'Insert nlines lines into the specified window above the current line',
               'window.insertln()': 'Insert a blank line under the cursor.',
               'windowinsnstr(varying set of parameters)': 'Insert a character string (as many characters as will fit on the line) before the character under the cursor, up to n characters.',
               'windowinsstr(varying set of parameters)': 'Insert a character string',
               'window.instr(varying set of parameters)': 'Return a bytes object of characters',
               'window.is_linetouched(line)': 'Return True if the specified line was modified',
               'window.is_wintouched()': 'Return True if the specified window was modified',
               'window.keypad(flag)': 'If flag is True, escape sequences generated by some keys',
               'window.leaveok(flag)': 'If flag is True, cursor is left where it is on update',
               'window.move(new_y, new_x)': 'Move cursor to (new_y, new_x).',
               'window.mvderwin(y, x)': 'Move the window inside its parent window. ',
               'window.mvwin(new_y, new_x)': 'Move the window so its upper-left corner is at (new_y, new_x).',
               'window.nodelay(flag)': 'If flag is True, getch() will be non-blocking.',
               'window.notimeout(flag)': 'If flag is True, escape sequences will not be timed out.',
               'window.noutrefresh()': 'Mark for refresh but wait.',
               'window.overlay()': 'Overlay the window on top of destwin',
               'window.overwrite()': 'Overwrite the window on top of destwin.',
               'window.putwin(file)': 'Write all data associated with the window into the provided file object',
               'window.redrawln(beg, num)': 'Indicate that the num screen lines, starting at line beg, are corrupted',
               'window.redrawwin()': 'Touch the entire window',
               'window.refresh()': 'Update the display immediately ',
               'window.resize(nlines, ncols)': 'Reallocate storage for a curses window to adjust its dimensions to the specified values. ',
               'window.scroll([lines=1])': 'Scroll the screen or scrolling region upward by lines lines.',
               'window.scrollok(flag)': 'Control what happens when the cursor of a window is moved off the edge',
               'window.setscrreg(top, bottom)': 'Set the scrolling region from line top to line bottom',
               'window.standend()': 'Turn off the standout attribute.',
               'window.standout()': 'Turn on attribute A_STANDOUT.',
               'window.subpad(varying set of parameters)': 'Return a sub-window',
               'window.subwin(varying set of parameters)': 'Return a sub-window, whose upper-left corner is at (begin_y, begin_x), and whose width/height is ncols/nlines.',
               'window.syncdown()': 'Touch each location in the window that has been touched in any of its ancestor windows. ',
               'window.syncok(flag)': 'If flag is True, then syncup() is called automatically whenever there is a change in the window',
               'window.syncup()': 'Touch all locations in ancestors of the window',
               'window.timeout(delay)': 'Set blocking or non-blocking read behavior for the window.',
               'window.touchline()': 'Pretend count lines have been changed, starting with line start',
               'window.touchwin()': 'Pretend the whole window has been changed, for purposes of drawing optimizations.',
               'window.untouchwin()': 'Mark all lines in the window as unchanged since the last call to refresh().',
               'window.vline(varying set of parameters)': 'Display a vertical line starting at (y, x) with length n consisting of the character ch.',}

def blue_print(text):
    return '\033[34m' + text + '\033[00m'

def purple_print(text):
    return '\033[35m' + text + '\033[00m'

for key, val in detail_dict.items():
    print(blue_print(key) + ' : ' + purple_print(val))

print(len(detail_dict.items()))