import view
import model
import logging


# если хотим, чтобы логи выводились в консоль
# logging.basicConfig(level=logging.INFO)


# если хотим, чтобы логи записывались в файл
logging.basicConfig(filename='log.txt',encoding="UTF-8",
filemode='a',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%H:%M:%S',
level=logging.WARNING)


def main_function():

    num = None
    while 1:
        num = view.show_menu()
        if num == "": 
            logging.warning("Принудительное завершение работы программы")
            break
        if int(num) == 1:
            logging.info("Выбран 1 пункт")
            view.show_employee(model.get_list())
        #    print(*model.get_list(), sep = "\n")
        elif int(num) == 2:
            logging.info("Выбран 2 пункт")
            model.create_employee(view.get_date())
        elif int(num) == 3:
            logging.info("Выбран 3 пункт")
            model.update_employee(view.select_row_employee())
        elif int(num) == 4:
            logging.info("Выбран 4 пункт")
            model.delite_employee(view.delete())
        elif int(num) == 5:
            logging.info("Выбран 5 пункт")
            model.overwrite_new_file(view.get_file_name())