#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:17:50 2018

@author: bradenaltstatt
"""

annual_salary = float(input("Please state your annual salary: "))

portion_saved = (float(input("Please state percentage of salary saved each month: ")))/100

total_cost = float(input("Please state the total cost of your dream home: "))

monthly_salary = annual_salary/12

portion_down_payment = total_cost * 0.25

current_savings = 0

r = 0.04

numMonths = 0

while portion_down_payment >= current_savings:
    current_savings += current_savings*(r/12)
    current_savings += monthly_salary * portion_saved
    print("current savings: ", current_savings)
    numMonths += 1
    
print("Number of months: ", numMonths)
print ("Number of years: ", numMonths/12)