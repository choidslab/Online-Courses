# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:07:11 2020
@author: TimChoi
"""

# for loops
# for i in range(10): # 'range' creates an iterator -> in this case a series of values 0~9
#     print(i)

# for i in range(10): 
    # print(i, end=' ') # end='' -> without new line

# for i in range(1, 10): # set a start num
#     print(i, end=' ')
 
# for i in range(1, 11): 
#     print(i, end=' ')
    
# for i in range(0, 101, 4):
#     print(i, end=' ')

# word = 'python'

# for char in word:
#     print(char)

# n = 10

# while n > 0:
#     print(n)
#     n -= 1

# user_input = int(input('Please enter ages of class member(Type -1 to end): '))
# ages = []
# while user_input > 0:
#     ages.append(user_input)
#     user_input = int(input('The next ages: '))

# print('The ages are', ages)

# count = 0
# class_names = []

# name = input('Please enter name type n to stop: ')
# while name != 'n':
#     count += 1
#     class_names.append(name)
#     print(f'{name} has been added.')
#     name = input('Next name?: ')

# print(f'There are {count} people in the class, they are {class_names}')