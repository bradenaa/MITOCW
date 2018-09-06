#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:31:55 2018

@author: bradenaltstatt
"""

numbersLeft = 10;
lastGreatestOddInput = 2;

while (numbersLeft > 0):
    print("There are " + str(numbersLeft) + " integers remaining");
    currentStrInput = input("Please enter another integer: ");
    currentInput = int(currentStrInput);
    
    if currentInput%2 != 0 and currentInput>lastGreatestOddInput:
        lastGreatestOddInput = currentInput;
    numbersLeft = numbersLeft - 1;
    
    
if lastGreatestOddInput == 2:
    print("There were no odd inputs entered");
else:
    print("The greatest odd number entered was :", str(lastGreatestOddInput))