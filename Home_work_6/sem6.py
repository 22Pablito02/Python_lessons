import math
from random import randint as rnd
from functools import reduce
# 1 Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.

# def get_num():
#     print("Введите числа:\nЧтобы остановить нажмите Enter")
#     sheet = []
#     while 1:
#         temp = input()
#         if temp == "": return sheet
#         else:
#             sheet.append(int(temp))

# print(reduce(math.gcd, get_num()))


# 2 Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

def quantity_cast():
    quantity = int(input("Введите кол-во бросков монетки: "))
    sheet = ""
    for i in range(0,quantity):
        if rnd(1,2) == 1: 
            sheet += "O" 
        else:
            sheet += "Р" 
    print(sheet)
    return sheet

def fiend_max_p(resSheet):
    count = 0
    temp = 0
    for i in range(0, len(resSheet)):
        if resSheet[i] != "Р":
            if temp < count:
                temp = count
            count = 0
        elif resSheet[i] == "Р":
            count +=1
    print(temp)

fiend_max_p(quantity_cast())