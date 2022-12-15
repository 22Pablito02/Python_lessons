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

from collections import Counter

arrView = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
# print(*arrView, sep = "\n")
arrWork = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
# print(*arrWork, sep = "\n")
finish = 0
countStep = 0

def PrintMatrix():
    print("\n")
    print(*arrView, sep = "\n")
    print()
    print(*arrWork, sep = "\n")
    print()

def SettingValue(token):
    PrintMatrix()
    ElNum = input(f"Введите цифру поля, куда хотите поставить {token}: ")
    for i in range(0, len(arrView)):
        for j in range(0, len(arrView[i])): 
            if arrView[i][j] == ElNum:
                arrView[i][j] = " " 
                arrWork[i][j] = token

while finish != 1:
    countStep += 1
    SettingValue("O")
    SettingValue("X")
    PrintMatrix()

    for i in range(0, len(arrWork)):
        if arrWork[i].count("X") == 3 or arrWork[i].count("O") == 3:
            print("Победа!")
            finish = 1
            break

    for j in range(0, len(arrWork)):
        Xsum = 0
        Osum = 0
        for i in range(0, 3):
            if arrWork[i][j] == "X":
                Xsum += 1
            elif arrWork[i][j] == "O":
                Osum += 1

        if Xsum == 3 or Osum == 3:
            print("Победа!")
            finish = 1
            break

    if  countStep > 6 and arrWork[0][0] == arrWork[1][1] == arrWork[2][2] or arrWork[0][2] == arrWork[1][2] == arrWork[2][0]:
        print("Победа!")
        finish = 1