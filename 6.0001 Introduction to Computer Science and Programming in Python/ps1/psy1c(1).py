#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:00:11 2018

@author: bradenaltstatt
"""

# set input variables
annual_salary = float(input("Please state your annual salary: "))

# starting conditions
cost_of_house = 1000000
semi_annual_raise = 0.07
r = 0.04
down_payment = (cost_of_house * 0.25)
targetMonths = 36
steps = 0

# bisection setup
low = 0
high = 10000
portion_saved = int((high + low) / 2)

found = False

while abs(low - high) > 1:
    
    # reset the starting conditions for the loop
    current_savings = 0
    numMonths = 0
    monthly_salary = annual_salary/(12)
    steps += 1
    
    print("**************************************************")
    print("Portion of monthly savings: ", portion_saved/10000)
    print("**************************************************")
    
    while numMonths != targetMonths:
        monthly_returns = current_savings*(r/12)
        monthly_savings = monthly_salary * (portion_saved / 10000)
        
        current_savings += (monthly_savings + monthly_returns)
        
        if abs(current_savings - down_payment) < 100:
            low = high
            found = True
            break
        elif current_savings > down_payment + 100:
            break # break out of current loop once savings is more than desired
        
        numMonths += 1
        print("- Months:", numMonths, "- Monthly Savings:", monthly_savings, "Monthly Returns:", monthly_returns, "- Current_savings:", current_savings,)
        # increase month and check if raise is implemented
        if numMonths % 6 == 0 and numMonths != 0:
            monthly_salary *= (semi_annual_raise + 1)
            print("Congrats! You got a raise")
        
    print("**************************************************")
    print("Savings after",  numMonths, "months: ", current_savings);
    print("**************************************************")
    print("-")
    print("-")
    print("-")
    
    if current_savings > down_payment + 100:
        high = portion_saved
        portion_saved = int((high + low) / 2)
    elif current_savings < down_payment - 100:
        low = portion_saved
        portion_saved = int((high + low) / 2)


if found:
    print("Best savings rate: ", portion_saved/ 10000)
    print("Steps in bisection search : ", steps)
else:
    print("It is not possible to save the down payment in three years")
        