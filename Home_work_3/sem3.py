import random

def ListSize():
    print("Введите размер списка:", end = " ")
    return int(input(""))

def FillList(size):
    list = []
    for i in range(0, size):
        temp = random.randint(0, 10)
        list.append(temp)
    return list

def PrintList(sheet):
    print(*sheet, sep = ", ")


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

sheet = FillList(ListSize())
PrintList(sheet)

def SumOdd(RList):
    sum = 0
    for i in range(0, len(RList)):
        if i % 2 != 0:
            sum += RList[i]
    print(sum)

SumOdd(sheet)



