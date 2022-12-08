import random
import math

def ListSize():
    return int(input("Введите размер списка: "))

def FillList(size):
    list = []
    for i in range(0, size):
        list.append(random.randint(0, 10))
    return list

def PrintList(sheet):
    print(*sheet, sep = ", ")

# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Введите число: "))
# res = []

# while n != 1:
#     i = 2
#     while 1:
#         if n % i == 0:
#             n = n / i
#             res.append(i)
#             break
#         else:
#             i += 1
# print (*res, sep = ", ")

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


sheet = [1,2,3,6,45,6,32,4,4,2,1]
res = []
for i in range(0, len(sheet)):
    if sheet.count(sheet[i]) == 1:
        res.append(sheet[i])
PrintList(res)