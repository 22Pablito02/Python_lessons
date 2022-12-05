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


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

sheet = FillList(ListSize())
PrintList(sheet)

# def SumOdd(RList):
#     sum = 0
#     for i in range(0, len(RList)):
#         if i % 2 != 0:
#             sum += RList[i]
#     print(sum)

# SumOdd(sheet)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

ResList = []
lenList = len(sheet)

if lenList % 2 != 0:
    lenList = lenList + 1
for i in range(0, lenList // 2):
    if i == lenList // 2:  
        ResList.append(sheet[i] * sheet[i])
    else:
        ResList.append(sheet[i] * sheet[-i-1])




PrintList(ResList)