import csv
import re

file = input()
with open(file, "r", encoding='utf_8-sig', newline='') as sfile:
    reader = csv.reader(sfile, delimiter=",")
    dict = {}
    list = [x for x in reader]
    columns = list[0]
    result = [x for x in list[1:] if len(x) == len(columns) and x.count("") == 0]
    for vacancy in result:
        for index, val in enumerate(vacancy):

            temp = re.sub(re.compile(r'<[^>]+>'),'', val)
            temp = temp.replace('\n', ', ')
            temp = temp.replace('\r\n', ', ')
            temp = ' '.join(temp.split())
            vacancy[index] = temp

        current_dict = {columns[i]: vacancy[i] for i in range(len(columns))}
        for key in current_dict.keys():
            print(f'{key}: {current_dict[key]}')
        print()
