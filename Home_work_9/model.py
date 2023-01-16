import sys, os, csv


def get_contact(update, context):
    lst = []
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        for row in file_read:
            lst.append(row)
   
    for i in range(0, len(lst)):
        temp = str(lst[i])    
        lool = ""
        for j in range(0, len(temp)):
            if temp[j] == "'" or temp[j] == "[" or temp[j] == "]": 
                lool += ""
            else:
                lool += temp[j]
        if i == 0:
            lool = "№, " + lool        
        else:
            lool = f"{i}) " + lool
        update.message.reply_text(lool)


def create_employee(update, context):
    lst = str(update.message.text).split(" ")
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(lst)
    update.message.reply_text("Контакт создан")


def delete_employee(update, context):
    num_row = int(update.message.text)
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        row = list(file_read)
        del row[num_row]
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for i in row:
            file_writer.writerow(i)
    update.message.reply_text("Контакт удален")


def update_employee(update, context):
    date = str(update.message.text).split(" ")
    num_row = int(date[0])
    del date[0]
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        row = list(file_read)
        row[num_row] = date
    with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for i in row:
            file_writer.writerow(i)
    update.message.reply_text("Пользователь изменен")