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

arrView = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
print(*arrView, sep = "\n")
print()
arrWork = [['x', '-', '-'],['-', '-', '-'],['-', '-', '-']]
print(*arrWork, sep = "\n")