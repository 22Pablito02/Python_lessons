import math
from functools import reduce
# 1 Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.

def get_num():
    print("Введите числа:\nЧтобы остановить нажмите Enter")
    sheet = []
    while 1:
        temp = input()
        if temp == "": return sheet
        else:
            sheet.append(int(temp))

print(reduce(math.gcd, get_num()))