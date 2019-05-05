import csv
import re
file_list=["info_1.txt", "info_2.txt", "info_3.txt"]
search = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

def get_data(file_name):
    res_dict={}
    with open (file_name, "r", encoding="cp1251") as f_n:
        for line in f_n:
            for el in search:
                if re.search(el, line):
                    result = re.findall(r':\s+(.+)', line)
                    res_dict[el]=result
        main_data = []
        main_data.append(list(res_dict.keys()))
        main_data.append(list(res_dict.values()))
        
    return main_data

def write_to_csv():
    for i in file_list:
        res = get_data(i)
        with open("info.csv", "a") as f_n:
            f_n_writer = csv.writer(f_n)
            for row in res:
                f_n_writer.writerow(row)
            f_n.close()

write_to_csv()
with open("info.csv") as f_n:
    print(f_n.read())
