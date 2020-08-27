# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:30:44 2020

@author: Timchoi
"""

# Q1. Ask the user for the raius of a circle and then print the area 
radius = float(input('Enter a radius\n >>> '))
pi = 3.14159
area_of_circle = pi * radius**2
print(area_of_circle)

# Q2. Conver fahrenheit to celsius(화씨 -> 섭씨 온도 변환)
temp_of_fah = float(input('Enter the fahrenheit\n >>> '))
temp_of_cel = (temp_of_fah - 32) * (5 / 9)
print(temp_of_cel)

# Q3. Obtain the sum of two integers
num1 = int(input('Enter the first num: '))
num2 = int(input('Enter the second num: '))
print(str(num1) + ' + ' + str(num2) + ' = ', num1 + num2)

# Q4. Obtain the product of two integers
num1 = int(input('Enter the first num: '))
num2 = int(input('Enter the second num: '))
print(str(num1) + ' * ' + str(num2) + ' = ', num1 * num2)

# Q5. Bob, Ann, Jane and Ashwin want to order pizza. 
# they will each eat 4 slices of pizza. The pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed? 
total_pizza = 4 * 4 # number of person, slices of pizza
number_of_pizzas = (total_pizza + 5) // 6
print(number_of_pizzas)
left_slices_of_pizza = (number_of_pizzas * 6) - total_pizza
print(number_of_pizzas, needed_pizza)
