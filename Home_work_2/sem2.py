print("Введите число: ", end = "")
num = input("")
sum = 0
for i in range(0, len(num)):
#     if num[i] == "," or num[i] == ".":
#         continue
#     else:
#         sum = sum + int(num[i])

    if num[i].isdigit():
        sum = sum + int(num[i])

print(sum)