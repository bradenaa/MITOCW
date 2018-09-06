#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:34:40 2018

@author: bradenaltstatt
"""

s = '1.23,2.4,3.123,4.234,8.95';
total = 0;
numberForm = '';

for ch in s:
    if ch != ',':
        numberForm = numberForm + ch;
    elif ch == ',':
        total = float(numberForm) + total;
        numberForm = '';
        

total = float(numberForm) + total;
print("The total comes to :", total);