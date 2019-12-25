# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:03:03 2019

@author: Jeremy Scharf
"""

# Determine how long it will take you to save enough money to make the down payment

annual_salary = float(input("Starting annual salary: "))
portion_saved = float(input("Portion of salary to be saved: "))
total_cost = float(input("Cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 #Annual return

num_months = 0
while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12 + annual_salary * portion_saved / 12
    num_months += 1

print("Number of months: " + str(num_months))