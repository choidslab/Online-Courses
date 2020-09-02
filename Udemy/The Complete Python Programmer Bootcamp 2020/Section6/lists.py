# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:56:51 2020

@author: TimChoi
"""

# Lists - collection of data
# string에서 이미 다뤘던 것처럼 indexing, slicing을 이용한 elements 접근 가능

# data = [53 , 76, 25, 98, 56, 42, 69, 81]

# data_1 = []

# total = 0
# for num in data:
#     total += num
# print(total)

# for i, num in enumerate(data):
#     print(i, num)

# # BIF(Built-In Function)

# # max
# print(max(data))

# # min
# print(min(data))

# my_list = [1, 11, 21, 31, 41, 51]
# for i in range(6):
#     print(my_list[i])


# # Bubble Sort
# data_copy = data[:]

# for i in range(len(data_copy)):
#     for j in range(0, len(data_copy)-i-1):
#         if data_copy[j] > data_copy[j+1]:
#             data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]

# print(data_copy)
# print(sorted(data))


"""
list method
"""
# my_list = [34, 76, 58]
# my_list.append(100) # append() 함수 - list의 마지막에 value 추가
# print(my_list)

# my_list.remove(34) # remove() - parameter로 전달한 값을 list에서 삭제
# print(my_list)

# my_list.reverse() # reverse() - list 정렬순서를 역순으로
# print(my_list)

# my_list.extend([10, 20, 30]) # extend() - list에 여러개의 값을 추가 -> list 확장
# print(my_list)

# print(my_list.index(10)) # index() - parameter로 전달된 값의 index 반환
