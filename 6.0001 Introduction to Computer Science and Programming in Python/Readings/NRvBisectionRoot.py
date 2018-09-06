#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:01:52 2018

@author: bradenaltstatt
"""

x = 2158
epsilon = 0.01
numBisectionGuesses = 0
numNRGuesses= 0

low = 1.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print ('low =', low, 'high =', high, 'ans =', ans )
    numBisectionGuesses += 1
    if ans**2 < x:
        low = ans 
    else:
        high = ans
    ans = (high + low)/2.0
    

print (ans, 'is close to square root of', x)

guess = x/2.0

while abs(guess*guess - x) >= epsilon:
    guess = guess - (((guess**2) - x)/(2*guess))
    numNRGuesses += 1;
    
print (guess, 'is close to square root of', x)


print ('numBisectionGuesses: ', numBisectionGuesses)
print ('numNRGuesses: ', numNRGuesses)
