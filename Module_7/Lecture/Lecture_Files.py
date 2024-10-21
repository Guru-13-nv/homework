# Лекция №1
print('Hellow')  # Таблица символов ASCII
print(ord('H'))  # Номер символа 'H' в ASCII
# Переведём всю строку в символы
a = 'Hello'  # Строка
chars = []  # Массив символов
for i in a:  # Цикл для перевода строки в символы
    chars.append(ord(i))
print(chars)
# Перевод чисел в символы
s = ''  # Строка
for i in chars:  # Цикл для перевода символов в строку
    s += chr(i)
print(s)
print(hex(ord('h')))
bb = b'\68'
print(bb.decode())

# Лекция №2 Режимы открытия файлов:
from pprint import pprint  # Импорт библиотеки pprint дл лекции 2

name = 'Files.txt'
file = open(name, 'r', encoding='utf-8')  # r,w,a - режимы открытия файла (read,write,append)
print(file)
pprint(file.read()) # Читает файл
file.close()
#
name = 'Files2.txt'
file = open(name, 'w', encoding='utf-8')  # r,w,a - режимы открытия файла (read,write,append)
file.write('Hello world') # Запись в файл. Перезаписывает файл
# file.read() #Выводит ошибку
file.close()

name = 'Files2.txt'
file = open(name, 'a', encoding='utf-8')  # r,w,a - режимы открытия файла (read,write,append)
file.write('\nHello world2') # Добавляет запись в конец файла
file.write('\nHello world3')
file.close()
# режимов открытия файла намного больше.Все режимы открытия файлов можно посмотреть в документации

name = 'Files2.txt'
file = open(name, 'r', encoding='utf-8')  # r,w,a - режимы открытия файла (read,write,append)
print(file.tell()) # Текущая позиция в файле
pprint(file.read()) # Читает файл
print(file.tell())
print(file.seek(20))
pprint(file.read())
file.close()

#Лекция №3 Позиционирование в файле:
import io
name = 'Files2.txt'
# file = open(name, 'w')
file = open(name, 'r')
print(file.tell()) # Текущая позиция в файле
pprint(file.read()) # Читает файл
file.close() # Закрывает файл
file = open(name, 'a') # Открывает файл в режиме append
print(file.tell()) # Текущая позиция в файле
file.seek(15) # Перемещает файл в указанную позицию
file.write('New Text') # Записывает в файл
print(file.tell()) # Текущая позиция в файле
file.close() # Закрывает файл

name = 'Files3.txt' # Создание файла
# file = open(name, 'w')
file = open(name, 'r', encoding='utf-8')
print(file.writable()) # Разрешение записи в файл
print(file.readable()) # Разрешение чтения из файла
print(file.seekable()) # Разрешение перемещения файла
print(file.name) # Имя файла
print(file.buffer) # Буфер
print(file.closed) # Файл закрыт
print(file.tell()) # Текущая позиция в файле
pprint(file.read()) # Читает файл
print(file.tell()) # Текущая позиция в файле
file.close() # Закрывает файл

#Lecture 4
#Оператор with
name = 'Files.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        # print(line) #Большое расстояние между строками из за считывания \n
        # print(line, end='')
        # Что бы пробежаться до конца файла и вывести каждый символ
        for char in line:
            print(char, end='')
    print(file.tell())