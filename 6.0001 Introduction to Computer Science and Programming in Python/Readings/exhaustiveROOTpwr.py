#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:34:52 2018

@author: bradenaltstatt
"""

intNum = int(input("Please enter an integer: "));
neg = False;

if intNum < 0:
    neg = True;

root = 0;
pwr = 2;

print("The integer is: ", intNum);
# Will always have at least one root/pwr such that intNum=root and pwr = 1
print ("rootFOUND: ", intNum, " pwrFOUND : ", 1);

while 0 < pwr < 6:
    while root**pwr <= abs(intNum):
#        print ("root: ", root, " pwr: ", pwr);
        if root**pwr == abs(intNum):
            if neg and pwr%2 != 0:
                print ("rootFOUND: ", -root, " pwrFOUND : ", pwr);
            elif not neg:
                print ("rootFOUND: ", root, " pwrFOUND : ", pwr);
        root += 1;
    pwr += 1;
    root = 0;




#while (currentInput != root**pwr):
#    print ("root: ", root, " pwr : ", pwr);
#    if pwr == 5:
#        pwr = 0;
#        root = root + 1;
#    
#    pwr = pwr + 1;
    
#print("The integer is : ", currentInput);
#print("The root is : ", root);
#print("The pwr is : ", pwr);





