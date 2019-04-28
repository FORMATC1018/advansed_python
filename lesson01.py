# coding utf-8

print('''Задание 1
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.\n''')

def type_out(variable):
    print(variable)
    print(type(variable))


words_list_1 = ['разработка', 'сокет', 'декоратор']

for el in words_list_1:
    type_out(el)

words_list_1_unic = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for el in words_list_1_unic:
    type_out(el)

print('''\nЗадание 2
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.\n''')

words_list_2 = [b'class', b'function', b'method']

for el in words_list_2:
    type_out(el)
    print(len(el))


print('''\nЗадание 3
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.\n''')

words_list_3 = ['attribute', 'класс', 'функция', 'type']
for el in words_list_3:
    if (el != el.encode("ascii", "ignore").decode("ascii")):
        print('Значение "{}" - невозможно перевести в байт тип'.format(el))



print('''\nЗадание 4
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).\n''')

words_list_4 = ['разработка', 'администрирование', 'protocol', 'standard']
for el in words_list_4:
    print(
        'Байтовое представление через encode - {}\n'.format(el.encode()) +
        'Возврат в исходное представление через decode - {}\n'.format(el.encode().decode())
    )
    

print('''\nЗадание 5
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.\n''')

import subprocess

data_0 = ['ping', 'yandex.ru']
data_1 = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(data_0, stdout=subprocess.PIPE)
for el in subproc_ping.stdout:
    el = el.decode('cp866').encode('utf-8')
    print(el.decode('utf-8'))

subproc_ping = subprocess.Popen(data_1, stdout=subprocess.PIPE)
for el in subproc_ping.stdout:
    el = el.decode('cp866').encode('utf-8')
    print(el.decode('utf-8'))

print('''\nЗадание 6
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.\n''')

with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write(
        'сетевое программирование\n' +
        'сокет\n' + 
        'декоратор'
    )
    print(type(f))


with open("test_file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)