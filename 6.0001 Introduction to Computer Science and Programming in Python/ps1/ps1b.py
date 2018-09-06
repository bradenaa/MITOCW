#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 12:41:32 2018

@author: bradenaltstatt
"""

annual_salary = float(input("Please state your annual salary: "))

portion_saved = (float(input("Please state percentage of salary saved each month: ")))/100

total_cost = float(input("Please state the total cost of your dream home: "))

semi_annual_raise = (float(input("Please state the percentage increase you plan to receive every 6 months: ")))/100

monthly_salary = annual_salary/12

portion_down_payment = total_cost * 0.25

current_savings = 0

r = 0.04

numMonths = 0

while portion_down_payment >= current_savings:
    # last months returns get added to current savings first
    current_savings += current_savings*(r/12)
    # each month a certain amount gets saved from portion of your salary
    current_savings += monthly_salary * portion_saved
    print("current savings: ", current_savings)
    numMonths += 1
    # a raise is initialized prior to the start of the next month if it is the end of 6 month interval
    if numMonths % 6 == 0:
        monthly_salary *= (semi_annual_raise + 1)
    
print("Number of months: ", numMonths)
print ("Number of years: ", numMonths/12)

