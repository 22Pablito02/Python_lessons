def show_menu():
    num = input("\n1 - показать всех сотрудников;\n2 - добавить сотрудника;\n3 - изменить данные сотрудника;\n4 - удалить сотрудника.\n5 - перезапись в новый файл\n")
    try:
        num = int(num)
    except:
        print("Введено не число!")
        num = ""
    return num


def show_employee(lst):
    print("")
    for i, man in enumerate(lst, 0):
        if i == 0:
            print("№", *man)
        else:
            print(i, *man)


def get_date():
    name = input("Введите Имя: ")
    surname = input("Введите Фамилию: ")
    mobile = input("Введите Номер: ")
    try:
        mobile = int(mobile)
    except:
        mobile = input("Некоректный номер! Введите номер еще раз: ")
    post = input("Введите Должность: ")
    lst = [name,surname,mobile,post]
    return lst


def select_row_employee():
    num_row = int(input("Введиете строку перезаписи: "))
    print("Введите Изменяемые данные: ")
    name = input(" Имя: ")
    surname = input(" Фамилию: ")
    mobile = input(" Номер: ")
    try:
        mobile = int(mobile)
    except:
        mobile = input("Некоректный номер! Введите номер еще раз: ")
    post = input(" Должность: ")
    lst = [name,surname,mobile,post]
    return num_row, lst


def delete():
    num_row = int(input("Введиете строку удаления: "))
    return num_row


def get_file_name():
    file_name = input("Введите имя нового файла: ")
    return file_name
