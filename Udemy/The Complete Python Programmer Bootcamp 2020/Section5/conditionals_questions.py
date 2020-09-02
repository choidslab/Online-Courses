# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:09:37 2020

@author: TimChoi
"""

""""
Question 1 
- 사용자로부터 숫자(int)를 입력받아 해당하는 영단어로 출력
"""
# user_input = int(input('Enter the number: '))

# if user_input == 1:
#     print('One')
# elif user_input == 2:
#     print('Two')
# elif user_input == 3:
#     print('Three')
# elif user_input == 4:
#     print('Four')
# elif user_input == 5:
#     print('Five')
# else:
#     print('Reject!')


""""
Question 2 
- 사용자로부터 숫자 영단어를 입력받아 해당하는 숫자로 출력
"""

# user_input2 = input('Enter the string: ')

# user_input2 = user_input2.lower()

# if user_input2 == 'one':
#     print(1)
# elif user_input2 == 'two':
#     print(2)
# elif user_input2 == 'three':
#     print(3)
# elif user_input2 == 'four':
#     print(4)
# elif user_input2 == 'five':
#     print(5)
# else:
#     print('Reject!')

""""
Question 3 
- 임의의 지정된 숫자를 사용자가 예측하는 프로그램
"""

# guess_num = 8

# user_input = int(input('Enter the your guess number(1 ~ 10): '))

# if user_input == guess_num:
#     print('Correct number! You win!')
# elif user_input > guess_num and (0 <= user_input <= 10): # user_input > guess_num and user_input <= 10
#     print('you guessed too high. You lose!')
# elif user_input < guess_num and (0 <= user_input <= 10): # user_input < guess_num and user_input >= 1
#     print('you guessed too low. You lose!')
# else:
#     print('out of range!')


""""
Question 4 
- 사용자로부터 이름(string)을 입력받고, 문자열 길이가 5보다 큰 경우에만 길이 출력
"""

# user_name = input("What is your name? >>> ")
# len_user_name = len(user_name)
# if len_user_name > 5:
#     print('your name len: {}\n'.format(len_user_name))
# else:
#     print('I\'m not telling you the len of your name.')

""""
Question 5
- 사용자로부터 숫자 2개를 입력 받아 두 숫자가 모두 15보다 크면 곱셈을 반환하고 
둘 중 하나만 15보다 클 경우 합을 반환하고 둘 다 15보다 작으면 0을 반환
"""
# num1 = int(input('Enter the first num(1~20): '))
# num2 = int(input('Enter the second num(1~20): '))

# if (num1 > 15 and num2 > 15) and (num1 <= 21 and num2 <= 21):
#     print(num1 * num2)
# # elif ((num1 > 15 and num2 < 15) or (num1 < 15 and num2 > 15)) and (num1 <= 21 and num2 <=21):
# elif num1 > 15 or num2 > 15
#     print(num1 + num2)
# elif (num1 < 15 and num2 < 15) and (num1 >=1 and num2 >= 1):
#     print(0)
# else:
#     print('out of range')

"""
Question 6
- 사용자로부터 숫자 2개를 입력 받고, 이를  swap 한다.
"""
num1 = int(input('Enter the first num: '))
num2 = int(input('Enter the second num: '))

# Before Swap
print('Before Swapping - num1: ', num1, 'num2: ', num2)
# After Swap
num1, num2 = num2, num1
print('After Swapping - num1: ', num1, 'num2: ', num2)
