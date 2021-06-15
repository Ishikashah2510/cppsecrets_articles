# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:41:42 2021

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

detail_dict = {'curses.initscr()' : 'Initializes a new terminal',
               'curses.baudrate()' : "Returns the output speed of terminal in bits per second",
                'curses.beep()' : 'Emits a attention sound',
                'curses.can_change_color' : 'Returns True if the programmer can change color displayed by terminal else False',
                'curses.cbreak()' : 'Enters cbreak mode',
                'curses.color_content(color_number)' : 'color_number must be between 0 to colors-1. This function returns a 3 valued tuple representing the RGB colors',
                'curses.color_pair(pair_number)' : 'Returns the attirbute for displaying text in specified color pair ',
                'curses.curs_set(visibility)' : 'To set visibility to 0: invisible, 1: Normal, 2: very visible',
                'curses.def_prog_mode()' : 'Save current terminal mode as program mode',
                'curses.def_shell_mode()' : 'Save current terminal mode as shell mode',
                'curses.delay_output(ms)' : 'Delaying output by ms milliseconds',
                'curses.doupdate()' : 'To update the physical screen',
                'curses.echo()' : 'To enter echo mode',
                'curses.endwin()' : 'Return terminal to normal status',
                'curses.filter()' : 'To implement the filter routine',
                'curses.flash()' : 'To Flash the screen',
                'curses.flushinp()' : 'To flush all input buffers',
                'curses.getmouse()' : 'Returns queued mouse event',
                'curses.getsyx()' : 'Returns the current coordinates of the virtual screen cursor',
                'curses.getwin(file)' : 'Read window related data stored in the file',
               'curses.has_colors()' : 'Returns True if screen can display colors',
               'curses.has_ic()' : 'Returns True if terminal has insert and delete character capability',
               'curses.has_il()' : 'Returns True if terminal has insert and delete line capability',
               'curses.has_key(ch)' : 'Returns True if key in terminal, else False',
               'curses.halfdelay(x)' : 'Used for half-delay mode',
               'curses.init_color(color_number, r, g, b)' : 'To change the definition of a color',}

def blue_print(text):
    return '\033[34m' + text + '\033[00m'

def purple_print(text):
    return '\033[35m' + text + '\033[00m'

for key, val in detail_dict.items():
    print(blue_print(key) + ' : ' + purple_print(val))
