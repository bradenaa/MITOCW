#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:09:06 2018

@author: bradenaltstatt
"""

def isIn(x, y):
    if x in y:
        return True
    elif y in x:
        return True
    else:
        return False
    
print(isIn("homeower", "meow"))
print(isIn("meow", "homeowner"))
print(isIn("no", "yes"))

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # check if letter in secret_word is contained in the letters_guessed list
    for l in secret_word:
        if l not in letters_guessed:
            return False
    
    return True
        
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word, letters_guessed)

