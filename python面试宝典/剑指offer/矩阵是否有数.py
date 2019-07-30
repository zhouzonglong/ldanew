# import numpy as np
# arrays=[[1,2,3],[4,5,6],[7,8,9]]
# # m,n=np.array(arrays).shape
#
#
# def Find(target, array):
#     m, n = np.array(array).shape
#     i = 0
#     j = n - 1
#     while True:
#         if target == array[i][j]:
#             return True
#         elif target > array[i][j]:
#             if i < m - 1:
#                 i += 1
#             else:
#                 return False
#         else:
#             if j > 0:
#                 j -= 1
#             else:
#                 return False
# lists=[-1,2,3,4,5,6,7,8,9,10,11]
# for each in lists:
#
#     print(Find(each,arrays))
# from past.builtins import raw_input
# #
# # while True:
# #     try:
# #
# #         # 字符串转为list
# #         L=list(eval(raw_input()))
# #         array=L[1]
# #         target=L[0]
# #         print(array)
# #     except:
# #         break
# from past.builtins import raw_input
# age=eval(raw_input('输入年龄  '))
# rray=age[1]
# target=age[0]
# print(rray)
# print(target)

# [[1,2,3],[4,5,6],[7,8,9]]
from inspect import stack

from jieba import xrange
from matplotlib.cbook import Stack


# def rectCover(number):
#     # write code here
#     if number <= 1:
#         return 1
#     elif number == 2:
#         return 2
#     else:
#         sums = 0
#         a = 1
#         b = 1
#         for i in range(1, number):
#             print('*')
#             sums = a + b
#             a = b
#             b = sums
#     return sums
# for i in range(10):
# def rectCover2(number):
#     if number <= 0:
#         return 0
#     a, b = 1, 2
#     for index in xrange(number - 1):
#         b += a
#         a = b - a
#     return a
# def duplicate(numbers, duplication):
#     # write code here
#     dic = {}
#     for each in numbers:
#         if each in dic:
#             dic[each] += 1
#             if dic[each] > 1:
#                 duplication[0]=each
#                 print(duplication)
#                 return True
#         else:
#             dic[each] = 1
#     return False
# list=[2,3,10,2,5,3,1]
# lists=[-1]
# print(duplicate(list,lists))

# def Sum_Solution(n):
#     # write code here
#     return n + Sum_Solution(n - 1)
#
#
# print(Sum_Solution(4))

print(~5)









