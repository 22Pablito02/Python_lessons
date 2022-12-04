# print("Введите число: ", end = "")
# num = input("")
# sum = 0
# for i in range(0, len(num)):
# #     if num[i] == "," or num[i] == ".":
# #         continue
# #     else:
# #         sum = sum + int(num[i])

#     if num[i].isdigit():
#         sum = sum + int(num[i])

# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# print("Введите число: ", end = "")
# num = int(input(""))
# sum = 1
# lol = []

# for i in range(1,num + 1):
#     sum = 1
#     for j in range(1,i + 1):
#         sum = sum * j
#     lol.append(sum)
# print(*lol, sep = ", ")

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# import random
# n = random.randint(2,10)
# sheet = []
# sum = 0
# for i in range(1,n):
#     sum =   round((1 + 1 / i) ** i, 2)
#     sheet.append(sum)
# print(*sheet, sep = ", ")


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import os
# import sys
# print("Введите число: ", end = "")
# n = int(input(""))
# sheet = []
# result = 1
# for i in range(-n,n+1):
#     sheet.append(i)
# print("Промежуток значений:", *sheet, sep = " ")

# FileSheet = []
# f = open(os.path.join(os.path.dirname(sys.argv[0]),'text.txt'), 'r')
# a = f.read()
# for i in range(len(a)):
#     if a[i].isdigit():
#         FileSheet.append(a[i])
# print("Индексы из файла:", *FileSheet, sep = " ")

# for i in range(len(FileSheet)):
#     temp = int(FileSheet[i])
#     for j in range(len(sheet)):
#         if j == temp:
#             result = result * sheet[j]
#             break

# print("Ответ:", result)


# Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random
sheet = []
n = 10
for i in range(n + 1):
    sheet.append(random.randint(0,100)) 
print(*sheet, sep = ", ")
sheet.reverse()

for i in range(len(sheet)):
    temp = sheet[i]    
    ran = random.randint(0,10)
    sheet[ran] = temp
print(*sheet, sep = ", ")

