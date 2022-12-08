import os, sys
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

# Вычислить число c заданной точностью d
# import math
# num = input("Введите значение: ")
# print(round(math.pi , len(num.split('.')[1])))



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

# sheet = [1,2,3,6,45,6,32,4,4,2,1]
# res = []
# for i in range(0, len(sheet)):
#     if sheet.count(sheet[i]) == 1:
#         res.append(sheet[i])
# PrintList(res)


# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# k = int(input("Введите размер списка: "))
# sheet = []
# res = ""

# for i in range(0, k + 1):
#         sheet.append(random.randint(-100, 100))


# for i in range (0, len(sheet)):
#     if k == 0:
#             if sheet[i] > 0:
#                 res += "+" + str(sheet[i])
#             else:
#                 res += str(sheet[i])
#     elif k == 1:
#         if sheet[i] > 0:
#             res += "+" + str(sheet[i]) + "x"
#         else:
#             res += str(sheet[i]) + "x"
#     else:
#         if i == 0 and sheet[i] > 0 or sheet[i] < 0:
#             res += str(sheet[i]) + "x^" + str(k)
#         else:
#             res += "+" + str(sheet[i]) + "x^" + str(k)
#     k -= 1    
# res += "=0"
# NameForCreate = input("Введите имя файла для создания: ")

# def CreateFile(FileName, content):
#     with open(os.path.join(os.path.dirname(sys.argv[0]),FileName),"w") as file:
#         file.write(content)

# CreateFile(NameForCreate, res)



def ReadingFile():
    FileName = input("Введите имя файла для прочтения: ")
    content = None
    with open(os.path.join(os.path.dirname(sys.argv[0]),FileName),"r") as file:
        return file.read(content)

    
def SumСoefficient(content):
    print(content)
    content = content.strip('=0')

    for i in range(0, len(content)):
        temp = list(content)
        for j in range(0,len(temp) - 1):
            if temp[j] == "^":
                temp[j] = ""
                temp[j+1] = ""
    print(temp)
    lol = ""
    for i in range(0, len(temp)):  
        if temp[i].isdigit() or temp[i] == "x" or  "-" or "":
            lol += temp[i]
    print(lol)
    lol = lol.split("x")

    sum = 0
    for i in range(0, len(lol)):
        sum += int(lol[i])
    print(sum)
    return sum


# print(SumСoefficient(ReadingFile()) + print(SumСoefficient(ReadingFile())))

sum1 = SumСoefficient(ReadingFile())
sum2 = SumСoefficient(ReadingFile())
ResSum = sum1 + sum2
print(str(sum1) + " + " + str(sum2) + " = " + str(ResSum))