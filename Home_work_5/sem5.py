# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = ("забвение было абв мимолетным абвукп").split()

def lol(a):
    # for i in range(0, len(a)):
    #     if "абв" in a:
    if "абв" not in a:
        return a

# print(lol(text)) 
#  lambda x: not x == "абв"

sheet = list(filter(lol ,text))
print(sheet)