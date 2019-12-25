# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:25:10 2019

@author: Jeremy Scharf
"""

original_annual_salary = float(input("Starting annual salary: "))
down_payment = 250000
semi_annual_raise = 0.07
current_savings = 0
r = 0.04

steps = 0
low = 0.0
high = 1.0
saving_rate = (high + low) / 2.0

while abs(current_savings - down_payment) >= 100:
    current_savings = 0
    annual_salary = original_annual_salary
    for n in range(36):     
        current_savings += current_savings * r / 12.0 + annual_salary * saving_rate / 12.0
        if n % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    steps += 1
#    print (current_savings)
#    print(steps)
    if current_savings < down_payment:
        low = saving_rate
    else:
        high = saving_rate
    saving_rate = (high + low) / 2.0
    
    if steps > 1000:
        break

if steps > 1000:
    print("No possible solution")
else:
    print("Best savings rate: " + str(saving_rate))
    print("Number of steps in bisection search: " + str(steps))
    print("The savings are: " + str(current_savings))