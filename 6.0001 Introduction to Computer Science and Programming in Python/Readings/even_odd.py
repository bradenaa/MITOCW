#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 09:12:18 2018

@author: bradenaltstatt
"""

x = 70;
y = 10;
z= 2;

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x > y and x > z:
        print("x is the largest odd number: ", x);
    elif y > z:
        print("y is the largest odd number: ", y);
    else:
        print("z is the largest odd number: ", z);
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x > y:
        print("x is the largest odd number: ", x);
    else:
        print("y is the largest odd number: ", y);        
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x > z:
        print("x is the largest odd number: ", x);
    else:
        print("z is the largest odd number: ", z); 
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y > z:
        print("y is the largest odd number: ", y);
    else:
        print("z is the largest odd number: ", z);
elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print("x is the only and largest odd number: ", x);
elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print("z is the only and largest odd number: ", y);
elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print("z is the only and largest odd number: ", z);
else:
    print("All numbers are even")
