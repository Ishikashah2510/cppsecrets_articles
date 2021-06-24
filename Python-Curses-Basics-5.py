# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:52:41 2021

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
    
    string = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
    screen.addstr(0, 0, string)
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(10, 0, 'Clearing from 0, 13 to end of line')
    screen.refresh()
    curses.napms(3000)
    screen.move(0, 13)
    screen.clrtoeol()
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(11, 0, 'Deleting character at 4, 40')
    screen.refresh()
    curses.napms(3000)
    screen.move(4, 40)
    curses.napms(1000)
    screen.delch(4, 40)
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(12, 0, 'Deleting line 2')
    screen.refresh()
    curses.napms(3000)
    screen.move(2, 0)
    curses.napms(1000)
    screen.deleteln()
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(13, 0, 'Upper left coordinates : ' + str(screen.getbegyx()))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(14, 0, 'Reading a character from user : ')
    screen.refresh()
    inp_char = screen.getch()
    
    screen.addstr(15, 0, 'Character read in ascii: ' + str(inp_char))
    screen.addstr(16, 0, 'Character read : ' + chr(inp_char))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(17, 0, 'Reading a character from user using getkey(): ')
    screen.refresh()
    inp_char = screen.getkey()
    
    screen.addstr(18, 0, 'Character read: ' + str(inp_char))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(19, 0, 'Maximum size of window : ' + str(screen.getmaxyx()))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(20, 0, 'Reading a string from user: ')
    screen.refresh()
    inp_char = screen.getstr()
    
    screen.addstr(21, 0, 'string read: ' + str(inp_char))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(22, 0, 'Character at 2, 10 is : ' + chr(screen.inch(2, 10)))
    screen.refresh()
    curses.napms(3000)
    
    screen.addstr(23, 0, 'Adding character "x" at 2, 10')
    screen.refresh()
    curses.napms(3000)
    screen.insch(2, 10, 'x')
    screen.refresh()
    curses.napms(3000)
    
    curses.endwin()


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> screen.clrtoeol()
        -> screen.delch()
        -> screen.deleteln()
        -> screen.getbegyx()
        -> screen.getch()
        -> screen.getkey()
        -> screen.getmaxyx()
        -> screen.getstr()
        -> screen.inch()
        -> screen.insch()
        -> screen.addstr()
        -> screen.refresh()
        -> curses.initscr()
        -> curses.napms()
        -> curses.endwin()

Link for output
https://youtu.be/F9mkhj80KJ4
"""
