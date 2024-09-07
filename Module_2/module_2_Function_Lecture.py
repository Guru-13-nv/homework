# Функция
# Функция - специальной блок кода который можно вызвать множество раз

'''Обычная функция'''


def sey_hello():  # Обычная функция
    print('Hello')


# Вызов функции производится:
sey_hello()
sey_hello()
sey_hello()

'''Принимающая функция'''


# Принимающая функция
def say_hello_1(name):
    print('Hello', name)


# Вызов функции с параметром
say_hello_1('Max')

'''Возвращающая функция'''
# Возвращающая функция
import random  # импорт библиотеки


def lottery():  # Функция лотерея
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список значений
    win = random.choice(tickets)  # Метод для рандомного выбора числа из переданного в него списка
    return win  # После команды return функция прекращает выполнение


win = lottery()
print(win)
win = lottery() + lottery()
print(win)

'''Возвращающе - принимающие функции'''


def lottery(mon, thue):  # Функция лотерея
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список значений
    win1 = random.choice(tickets)  # Метод для рандомного выбора числа из переданного в него списка
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2  # После команды return функция прекращает выполнение


win1, win2 = lottery('mon', 'thue')
print(win1, win2)


# Если не знаем сколько параметров будет принимать функци то: *args - для обычных параметров
# **kwargs - для именованных параметров
def lottery(*args, **kwargs):  # Функция лотерея
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список значений
    win1 = random.choice(tickets)  # Метод для рандомного выбора числа из переданного в него списка
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2  # После команды return функция прекращает выполнение


win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(win1, win2)

'''Значения по умолчанию в принимающих функциях'''


def test(a=2, b=True):
    print(a, b)


test()
test(False, 'ok')  # переназначение параметров по умолчанию

'''Распаковка в качестве параметров список или словарь
рассмотрим на примере списка'''


def test_1(a=2, b=True):
    print(a, b)


test_1([1, 2])  # Распаковка значения
test_1(*[1, 2])  # Распаковка списка
test_1(**[1, 2])  # Распаковка словаря
