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

# sheet = FillList(ListSize())
# PrintList(sheet)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.



# def SumOdd(RList):
#     sum = 0
#     for i in range(0, len(RList)):
#         if i % 2 != 0:
#             sum += RList[i]
#     print(sum)

# SumOdd(sheet)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# ResList = []
# lenList = len(sheet)

# if lenList % 2 != 0:
#     lenList = lenList + 1
# for i in range(0, lenList // 2):
#     if i == lenList // 2:  
#         ResList.append(sheet[i] * sheet[i])
#     else:
#         ResList.append(sheet[i] * sheet[-i-1])
# PrintList(ResList)



# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


# def FillListFloat(size):
#     list = []
#     for i in range(0, size):
#         list.append(round(random.uniform(0, 10), 2))
#     return list


# sheet = FillListFloat(ListSize())
# PrintList(sheet)
# for i in range(0, len(sheet)):
#     sheet[i] = round(sheet[i] - int(sheet[i]), 2)
# PrintList(sheet)
# print(max(sheet) - min(sheet)) 


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input("Введите число:"))
print("\nДесятичное число: ", num)
numBin = format(num, 'b')
print("Двоичное число: ", numBin)

