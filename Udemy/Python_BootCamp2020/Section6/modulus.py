# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:34:16 2020

@author: TimChoi
"""
# modulus calculation, num1 % num2 
# Fizzbuzz
# If a number is divisible by 3 -> Fizz
# If a number is divisible by 5 -> Buzz
# If a number is divisible by 3 & 5 -> FizzBuzz

n = 100

for i in range(1, n + 1): # if 조건문의 순서가 중요!
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    else:
        print(i)

# 아래의 경우 FizzBuzz가 절대로 출력되지 않음
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, 'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz')
    else:
        print(i)
