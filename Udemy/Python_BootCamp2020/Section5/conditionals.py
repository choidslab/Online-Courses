#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:23:18 2020

@author: dooseop
"""

# Boolean 

x = 5
y = 6

print('x = ', x, 'y = ', y)
print('Checking less than with \'<\':', x < y)
print('Checking greater than with \'>\':', x > y)
"""
[출력결과]
x =  5 y =  6
Checking less than with '<': True
Checking greater than with '>': False
"""

var_1 = 7
var_2 = 7

print('var_1 = ', var_1, 'var_2 = ', var_2)
print('Checking equaltiy than with \'==\':', var_1 == var_2)
print('Checking not equal than with \'==\':', var_1 != var_2)
print('Checking less than or equal with \'==\':', var_1 <= var_2)
print('Checking greater than or equal with \'==\':', var_1 >= var_2)

"""
[출력결과]
var_1 =  7 var_2 =  7
Checking equaltiy than with '==': True
Checking not equal than with '==': False
Checking less than or equal with '==': True
Checking greater than or equal with '==': True
"""

print(type(True)) # bool

# Logical Operators
var_3, var_4, var_5 = 15, 20 , 25

print('var_3 =', var_3, 'var_4 =', var_4, 'var_5 =', var_5)
print('var_4 and var_5 < 100?', var_4 < 100 and var_5 < 100)
print('var_4 and var_5 < 22?', var_4 < 22 and var_5 < 22)
print('var_4 and var_5 < 22?', var_4 < 22 or var_5 < 22)
