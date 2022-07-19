import csv

open_txt = open("./data.txt", "rt", encoding='UTF8')
write_csv = open("./ouput.txt", "wt", encoding="UTF8")

lines = open_txt.readlines()
output_csv = open("./output.csv", "a")
wr = csv.writer(output_csv, quoting=csv.QUOTE_ALL)
cnt=0
for i in lines:
    i = i.strip()
    i+=","
    cnt += 1
    if cnt % 7 == 0:
        i = i[:-1]
        i += "\n"
    write_csv.write(i)
    