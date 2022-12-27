import csv
import os
import sys


def read_file_txt(): 
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"test.txt"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
    return lst



def write_list_txt(lst):
    with open(os.path.join(os.path.dirname(sys.argv[0]),"test.txt"),"a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(lst)
        # for row in lst:
        #     file_writer.writerow(row)



def read_file_csv():
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"fcsv_res.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
    return lst



def write_list_csv(lst):
    with open(os.path.join(os.path.dirname(sys.argv[0]),"fcsv_res.csv"),"a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(lst)
        # for row in lst:
        #     file_writer.writerow(row)
    
