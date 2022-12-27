import view
import model

def main_function():
    num = None
    while 1:
        num = view.greeting()
        if num == "": break
        elif int(num) == 1:
            model.write_list_csv(view.get_values())
        elif int(num) == 2:
            model.write_list_txt(view.get_values())
        elif int(num) == 3:
            print(*model.read_file_csv(), sep = "\n")
        elif int(num) == 4:
            print(*model.read_file_txt(), sep = "\n")
    