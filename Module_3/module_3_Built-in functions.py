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
names = ['Denis', 'Anton', 'Egor', 'Katya', 'Jenya']
zipped = dict(zip(names, salary))
print(list(zipped))
print(zipped['Denis'], '-Зарплата Дениса')
# Часть 2
# Any()
# all()
a = [True, False, False]
print(any(a))  # Пробегается по списку и вернёт True, если есть хоть 1 True
# Все числа будут возвращать True, кроме нуля
# Применительно к строкам - если в троке есть даные, то True, если нет False

# all
a = [1, 1, 0]
b = ''
print(all(a))
# Функция ALL обратна any, если все этлементы True - вернёт True, если хоть один
# элемент будет False - вернёт False

# Интроспекция -Возможность запросить тип и структуру объекта во время выполнения программы.
# Dir
print(dir(a))  # Методы работы с программой
print(dir(a))
print(isinstance(b, str))  # Проверка класса объекта
d = [1, 1, 0]
print(a == d)
print(a is d)
c = d
# id - функция для получения объекта в памяти
print(id(c))
print(id(d))
# функция help - справка о объекте, документация
print(help(a))


# Такое достигает за счёт строк документирования doc string
def helper():
    '''

    Эта функция-помощник

    '''
    pass


print(help(helper))
print(helper.__doc__)
