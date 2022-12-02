# print("Введите число: ", end = "")
# num = input("")
# sum = 0
# for i in range(0, len(num)):
# #     if num[i] == "," or num[i] == ".":
# #         continue
# #     else:
# #         sum = sum + int(num[i])

#     if num[i].isdigit():
#         sum = sum + int(num[i])

# print(sum)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print("Введите число: ", end = "")
num = int(input(""))
sum = 1
lol = []

for i in range(1,num + 1):
    sum = 1
    for j in range(1,i + 1):
        sum = sum * j
    lol.append(sum)
print(*lol, sep = ", ")
