
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# print("Введите число от 1 до 7:", end = " ")
# day = int(input(""))
# if day < 0 or day > 7:
#     print("Вы ввели число все интервала")
# elif day == 6 or day == 7:
#     print("Вы попали в выходной день недели!")
# else:
#     print("Вы попали в рабочий день")

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# print("\nЧто выхотите узнать:\n 1 - Номер плоскости по значениям координат.\n 2 - Диапазон точек по заданной четверти. ")
# num = int(input(""))
# if num == 1:
#     print("Введите значение координаты X:", end = " ")
#     x = float(input(""))
#     print("Введите значение координаты Y:", end = " ")
#     y = float(input(""))

#     if x > 0 and y > 0:
#         print("1 четверть")
#     elif x < 0 and y > 0:
#         print("2 четверть")               
#     elif x < 0 and y < 0:
#         print("3 четверть")
#     else:
#         print("4 четверть")

# if num == 2:
#     print("Введите номер плоскости", end = " ")
#     area = int(input(""))
#     if area > 4 and area < 0:
#         print("Введенное вами значениене не соответствует ни одному номеру плоскости")
#     elif area == 1:
#         print("X > 0; Y > 0")
#     elif area == 2:
#         print("X < 0; Y > 0")               
#     elif area == 3:
#         print("X < 0; Y < 0")
#     else:
#         print("X > 0; Y < 0")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# print("Введите координаты точки A",)
# DotAX = int(input(""))
# DotAY = int(input(""))
# print("Введите координаты точки B",)
# DotBX = int(input(""))
# DotBY = int(input(""))

# SegmentX = DotAX - DotBX
# SegmentY = DotAY - DotBY

# edge = round((SegmentX ** 2 + SegmentY ** 2) ** 0.5, 2)
# print(edge)

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z , end = " ")
            print(not (x or y or z) == (not x and not y and not z))