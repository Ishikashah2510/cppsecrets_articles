# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:05:44 2021

@author: Ishika
"""

"""
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.


In this article, I will be showing how to make the number guessing game using curses.

The first step would be to install curses module.
cmd command : 
    pip install windows-curses


It is recommended to run this code file in the command prompt by using 'python filename.py' command.

Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""


import curses
import random

if __name__ == "__main__":
    screen = curses.initscr()
    screen.addstr(0, 0, "Let's play the number guess game!")
    screen.addstr(1, 0, 'The number is between 0 to 500')
    screen.addstr(2, 0, 'You get 10 guesses to guess the right number!')
    screen.refresh()
    curses.napms(3000)
    y = 3
    guess_num = 1
    random_num = random.randint(0, 500)
    
    while True:
        screen.addstr(y, 0, 'Enter your guess : ')
        y += 1
        screen.refresh()
        inp_num = screen.getstr()
        if int(inp_num) < random_num:
            screen.addstr(y, 0, 'Number is greater than your guess')
            screen.refresh()
            y += 1
        elif int(inp_num) > random_num:
            screen.addstr(y, 0, 'Number is lesser than your guess')
            screen.refresh()
            y += 1
        else:
            screen.addstr(y, 0, 'Your guess is correct! You win')
            screen.refresh()
            y += 1
            break
        guess_num += 1
        if guess_num == 11:
            screen.addstr(y, 0, 'Actual number was ' + str(random_num))
            screen.refresh()
            y += 1
            break
    
    screen.addstr(y, 0, 'Thank you for playing!')
    screen.refresh()
    curses.napms(3000)
    curses.endwin()



"""
What did we use?
-> screen.addstr()
-> screen.refresh()
-> screen.getstr()
-> curses.initscr()
-> curses.endwin()
-> curses.napms()
"""