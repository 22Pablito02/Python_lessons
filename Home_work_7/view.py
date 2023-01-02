def greeting():
    num = input("\nВыберите действие, которое хотите выполнить:  \n1 - записать данные в файл csv; \n2 - записать данные в файл txt; \n3 - взять данные из файла csv; \n4 - взять данные из файла txt.\nЕсли хотите завершить, нажмите Enter\n ")
    return num


def get_values():
    surneme = input("Введите фамилию: ")
    name = input("Введите имя: ")
    tel = input("Введите номер: ")
    sheet = [surneme, name, tel]
    return sheet
