# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 09:53:37 2021

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
    curses.use_default_colors()
    
    screen.addstr(0, 0, 'Color content for 4 is : ' + str(curses.color_content(4)))
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(1, 0, 'Changing color content for 4')
    screen.refresh()
    curses.init_color(4, 255, 255, 0)
    screen.addstr(2, 0, 'Color content for 4 is : ' + str(curses.color_content(4)))
    screen.refresh()
    curses.napms(2000)
    curses.init_color(4, 502, 0, 0)
    screen.clear()
    
    screen.addstr(0, 0, 'Hello there, the cursor is visible right now')
    screen.refresh()
    curses.napms(2000)
    
    curses.curs_set(0)
    screen.addstr(1, 0, 'The cursor is set to invisible right now')
    screen.refresh()
    curses.napms(2000)
    
    curses.curs_set(2)
    screen.addstr(2, 0, 'The cursor is set to very visible right now')
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(3, 0, 'current coordinates by curses.getsyx() : ' + str(curses.getsyx()))
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(4, 0, 'current coordinates by window.getyx() : ' + str(screen.getyx()))
    screen.refresh()
    curses.napms(2000)
    screen.clear()
    
    screen.addstr(0, 0, "A box will appear in 2 seconds")
    screen.refresh()
    curses.napms(2000)
    screen.box()
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(2, 2, 'The current background character is : ' + str(screen.getbkgd()))
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(3, 2, 'Setting background character as letter "C"')
    screen.refresh()
    curses.napms(1000)
    screen.bkgdset(67)
    screen.addstr(4, 2, 'The current background character is : ' + str(screen.getbkgd()))
    screen.refresh()
    curses.napms(2000)
    screen.bkgdset(32)
    screen.clear()
    
    screen.addstr(6, 2, 'Resizing window')
    screen.refresh()
    curses.napms(2000)
    screen.resize(10, 10)
    screen.refresh()
    screen.box()
    screen.refresh()
    curses.napms(2000)
    
    screen.addstr(2, 2, "Erasing window")
    screen.refresh()
    curses.napms(2000)
    screen.erase()
    screen.refresh()
    curses.napms(2000)
    
    print("curses.isendwin() before calling the function: ", curses.isendwin())
    
    curses.endwin()
    
    print("curses.isendwin() after calling the function: ", curses.isendwin())


"""
Conclusion:
    We saw the usage of the following functions in this article:
        -> window.box()
        -> window.resize()
        -> window.erase()
        -> window.getbkgd()
        -< window.bkgdset()
        -> window.getyx()
        -> window.refresh()
        -> window.addstr()
        -> curses.getsyx()
        -> curses.isendwin()
        -> curses.init_color()
        -> curses.curs_set()
        -> curses.color_content()
        -> curses.start_color()
        -> curses.initscr()
        -> curses.napms(ms)
        -> curses.endwin()

Link for output
https://youtu.be/2FBIqZWQbBE
"""