'''Встроенные функции'''
from tkinter.font import names

# int () --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()

# Другие встроенные функции
salary = [2300, 1800.80, 5000, 1234.58, 7500.12]
print(salary)
'''Напишем гибкую функцию, которая будет считать среднюю,
минимальную, максимальную зарплату в компании и выводит в словарь
данные'''
# Количество зарплат
print(sum(salary) / len(salary), 2)  # Встроенная функция SUM суммирут и находим среднюю ЗП
# Где 2 - количество знаков после запятой
# Есть функции MIN и MAX
print(round(max(salary)), '-Максимальная зарплата')
print(round(min(salary)), '-Минимальная зарплата')
names=['Denis', 'Anton', 'Egor', 'Katya', 'Jenya']
zipped = dict(zip(names, salary))
print(list(zipped))
print(zipped['Denis'], '-Зарплата Дениса')