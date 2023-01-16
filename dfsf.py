import sys, os, csv

date = str("2 Даниил Морозкин 4356356346 Хлюп").split(" ")
num_row = int(date[0])
del date[0]
# date = str(date)

# for i in range(0, len(date)):
# temp = str(date)    
# lool = ""
# for j in range(0, len(date)):
#             if date[j]  == "'" or date[j] == "[" or date[j] == "]": 
#                 lool += ""
#             else:
#                 lool += date[j]

with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"r", encoding='utf-8') as r_file:
        file_read = csv.reader(r_file, delimiter=",")
        row = list(file_read)
        row[num_row] = date
with open(os.path.join(os.path.dirname(sys.argv[0]),"file.csv"),"w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for i in row:
            file_writer.writerow(i)
