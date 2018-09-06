#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:11:23 2018

@author: bradenaltstatt
"""

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
            
    summation = 0
            
    for char in s:
        try:
            number = int(char)
            summation += number
        except ValueError:
            summation = summation
            
    return summation

print(sumDigits('a2b3c4d'))

def findAnEven(l):
    """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
    
    for n in l:
        if n%2 == 0:
            return n
    raise ValueError('findAnEven called with bad arguments')
            
numberList = [1, 3, 3, 4]

print(findAnEven(numberList))