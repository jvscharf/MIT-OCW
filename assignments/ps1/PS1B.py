# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:20:23 2019

@author: Jeremy Scharf
"""

annual_salary = float(input("Starting annual salary: "))
portion_saved = float(input("Portion of salary to be saved (percentage): "))
total_cost = float(input("Cost of your dream home: "))
semi_annual_raise = float(input("Semi-annual raise (percentage): "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 #Annual return

num_months = 0
while current_savings < portion_down_payment:        
    current_savings += current_savings * r / 12 + annual_salary * portion_saved / 12
    num_months += 1
    if num_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months: " + str(num_months))