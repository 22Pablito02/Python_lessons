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

import random
n = random.randint(2,10)
sheet = []
sum = 0
for i in range(1,n):
    sum =   round((1 + 1 / i) ** i, 2)
    sheet.append(sum)
print(*sheet, sep = ", ")

