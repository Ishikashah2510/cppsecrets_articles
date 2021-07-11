# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:25:45 2021

@author: Ishika
"""

"""
The curses module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.


In this article, I will be showing how to make the hangman game using curses module.

The first step would be to install curses module.
cmd command : 
    pip install windows-curses


It is recommended to run this code file in the command prompt by using 'python filename.py' command.

Source Code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

import curses
import random


def start_game(word):
    screen = curses.initscr()
    
    screen.addstr(0, 0, 'Lets start hangman')
    screen.refresh()
    curses.napms(1000)
    
    guess_word = '_' * len(word)
    screen.addstr(1, 0, 'The length of the word is {}. Word : '.format(len(word)))
    screen.addstr(2, 0, guess_word)
    screen.refresh()
    curses.napms(1000)
    
    chances = 5
    okay = 0
    guess_word = list(guess_word)
    while chances > 0:
        screen.addstr(4, 0, 'Your guess please, {} chances left : '.format(chances))
        screen.refresh()
        inp_char = screen.getkey()
        if inp_char not in word:
            chances -= 1
            screen.addstr(3, 0, inp_char + ' not in word, try again')
            continue
        for x in range(len(word)):
            if word[x] == inp_char:
                guess_word[x] = inp_char
        
        
        screen.addstr(2, 0, ''.join(guess_word))
        screen.refresh()
        if ''.join(guess_word) == word:
            screen.addstr(5, 0, 'Congrats you won!')
            screen.refresh()
            okay = 1
            break
    
    if okay == 0:
        screen.addstr(5, 0, 'The word was : ' + word)
    screen.refresh()
    
    curses.napms(4000)
    curses.endwin()
            

if __name__ == '__main__':
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    # print(word)
    start_game(word)


"""
Conclusion:
    We used the following functions
    -> curses.initscr()
    -> curses.endwin()
    -> curses.napms()
    -> screen.refresh()
    -> screen.addstr()
    -> screen.getkey()

"""