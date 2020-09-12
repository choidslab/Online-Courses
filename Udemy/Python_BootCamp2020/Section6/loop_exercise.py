#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:37:53 2020

@author: TimChoi
"""

'''
Q1. Ask the user for two numbers between 1 and 100. 
Then count from the lower number to the higher number. 
Print the results to the screen.
'''

# num1 = int(input('Enter a first num(1~100): '))
# num2 = int(input('Enter a second num(1~100): '))

# while num1 < 1 or num2 < 1 or num1 > 100 or num2 > 100 or num1 == num2:
#     # input 값을 체크 -> 유효하지 않은 경우 계속해서 사용자 입력을 받도록 함
#     print('Invalid values! Try again.')
#     num1 = int(input('Enter a first num(1~100): '))
#     num2 = int(input('Enter a second num(1~100): '))

# if num1 < num2:
#     for i in range(num1, num2 + 1):
#         print(i)
# else:
#     for i in range(num2, num1 + 1):
#         print(i)


'''
Q2. Ask the user to input a string and then print it out to the screen in 
reverse order (use a for loop)
'''
word = input('Enter a word: ')
reverse_string = ''

for char in word:
    reverse_string = char + reverse_string

print(reverse_string)
