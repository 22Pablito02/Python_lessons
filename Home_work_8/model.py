import os, sys
import view
import csv

def get_list():
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
    return lst

def create_employee(lst):
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(lst)
     
def update_employee(num_row, new_date_employee):
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        row = list(file_read)
        row[num_row] = new_date_employee
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for i in row:
            file_writer.writerow(i)


def delite_employee(num_row):
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        row = list(file_read)
        del row[num_row]
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for i in row:
            file_writer.writerow(i)

def overwrite_new_file(file_name):
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
    with open(os.path.join(os.path.dirname(sys.argv[0]),file_name),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        # file_writer.writerow(lst)
        for row in lst:
            file_writer.writerow(row)