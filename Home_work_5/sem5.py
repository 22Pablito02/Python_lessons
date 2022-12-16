from random import randint as rnd 
import math

# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# text = ("забвение было абв мимолетным абвукп").split()

# sheet = list(filter(lambda x: "абв" not in x ,text))
# print(sheet)





# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


# def InputChek(num):
#     player = int(input(f"Ходит игрок №{num}: "))
#     while player > 28 or player <= 0 or player > AllSumСandies:
#         player = int(input("Вы ввели число больше 28! введите число еще раз: "))
#     return player 

# def gamerStep(AllSumСandies, num):
#     print("Конфет осталось: " + str(AllSumСandies))
#     player = InputChek(num)
#     AllSumСandies -= player
#     return AllSumСandies

# def BotStep(AllSumСandies):
#     print("Конфет осталось: " + str(AllSumСandies))
#     player = AllSumСandies % 29 if AllSumСandies % 29 != 0 else rnd(1,28)
#     print(f"Ходит Бот: {player}")
#     AllSumСandies -= player
#     return AllSumСandies


# AllSumСandies = int(input("Введите количество конфет: "))

# choice = int(input("Выберите с кем вы хотите играть: \n 1 - против игрока \n 2 - против бота\n"))
# if choice == 1:
#     Name1 = input("Игрок 1 ведите ваше имя: ")
#     Name2 = input("Игрок 2 ведите ваше имя: ")

#     StartPlayer = rnd(1,2)
#     if StartPlayer % 2 == 0:
#         print("Первым ходит: " + Name1)
#     else:
#         print("Первым ходит: " + Name2)

#     while AllSumСandies != 0:
        
#         AllSumСandies = gamerStep(AllSumСandies, 1)
#         if AllSumСandies == 0:
#             print("Выиграл игнок №1!")
#             break
#         AllSumСandies = gamerStep(AllSumСandies, 2)
#         if AllSumСandies == 0:
#             print("Выиграл игнок №2!")
#             break

# elif choice == 2:
#     while AllSumСandies != 0:
        
#         AllSumСandies = gamerStep(AllSumСandies, 1)
#         if AllSumСandies == 0:
#             print("Выиграл игнок!")
#             break
#         AllSumСandies = BotStep(AllSumСandies)
#         if AllSumСandies == 0:
#             print("Выиграл Бот!")
#             break



# 3 Создайте программу для игры в "Крестики-нолики"

# from collections import Counter

# arrView = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
# # print(*arrView, sep = "\n")
# arrWork = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
# # print(*arrWork, sep = "\n")
# finish = 0

# def PrintMatrix():
#     print("\n")
#     print(*arrView, sep = "\n")
#     print()
#     print(*arrWork, sep = "\n")
#     print()

# def GetValue(token):
#     UntiDuble = 0
#     ElNum = input(f"Введите цифру поля, куда хотите поставить {token}: ")
#     while UntiDuble != 1 or ElNum == "":
#         for i in range(0, len(arrView)):
#             if ElNum in arrView[i]: UntiDuble += 1
#         if ElNum == "": 
#             ElNum = input(f"Вы не выбрали цыфру!\nВведите цифру поля, куда хотите поставить {token}: ")
#         elif UntiDuble == 0:
#             ElNum = input(f"Такой цыфры нет!\nВведите цифру поля, куда хотите поставить {token}: ")
#     return ElNum

# def SettingValue(token):
#     PrintMatrix()
#     key = GetValue(token)
#     for i in range(0, len(arrView)):
#         for j in range(0, len(arrView[i])): 
#             if arrView[i][j] == key:
#                 arrView[i][j] = " " 
#                 arrWork[i][j] = token


# def VictoryCheck(finish):
#     for i in range(0, len(arrWork)):
#         if arrWork[i].count("X") == 3 or arrWork[i].count("O") == 3:
#             PrintMatrix()
#             print("Победа!")
#             finish = 1
#             break

#     for j in range(0, len(arrWork)):
#         Xsum = 0
#         Osum = 0
#         for i in range(0, 3):
#             if arrWork[i][j] == "X":
#                 Xsum += 1
#             elif arrWork[i][j] == "O":
#                 Osum += 1

#         if Xsum == 3 or Osum == 3:
#             PrintMatrix()
#             print("Победа!")
#             finish = 1
#             break

#     if  arrWork[0][0] == arrWork[1][1] == arrWork[2][2] != "-" or arrWork[0][2] == arrWork[1][1] == arrWork[2][0] != "-":
#         PrintMatrix()
#         print("Победа!")
#         finish = 1
#     return finish


# while 1:
#     SettingValue("O")
#     finish = VictoryCheck(finish)
#     if finish == 1:
#         break
#     SettingValue("X")
#     finish = VictoryCheck(finish)
#     if finish == 1:
#         break


# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os, sys
def ReadingFile():
    FileName = input("Введите имя файла для прочтения: ")
    content = None
    with open(os.path.join(os.path.dirname(sys.argv[0]),FileName),"r") as file:
        return file.read(content)

def WreatingFile(content):
    FileName = input("Введите имя файла для записи: ")
    with open(os.path.join(os.path.dirname(sys.argv[0]),FileName),"w") as file:
        file.write(content)

def coder(sheet):
    res = []
    count = 1
    el = ""
    for i in range(0,len(sheet)):
        if i == len(sheet) - 1:
            res.append(count)
            res.append(sheet[i])
        elif sheet[i] == sheet[i+1] and i != len(sheet) - 1:
            count += 1
            el = sheet[i]
        elif sheet[i] != sheet[i+1]:
            res.append(count)
            res.append(sheet[i])
            count = 1
            el = ""
            
    res = str(res)
    temp = ""
    for i in range(0, len(res)): 
        if res[i].isdigit() or res[i].isalpha():
            temp += res[i]
    return temp

#Шифрование и запись
code = ReadingFile().upper()
# sheet = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
code = coder(code)
print(code)
WreatingFile(code)

# Дешифрование
def decoder(sheet):
    temp = ""
    num = ""
    for i in range(0, len(sheet)): 
        if sheet[i].isdigit():
            num += sheet[i]
        elif sheet[i].isalpha():
            for j in range(0, int(num)):
                temp += sheet[i]
            num = ""
    return temp

code = decoder(ReadingFile().upper())
print(code)

