'''Способы вызова функции. Ошибки при вызове функции'''
from Module_1.Variables import course_name


# Простая функция
def print_parms(a, b, c):
    print(a, b, c)


# print_parms() - Вызовет ошибку т.к. не переданы параметры
print_parms('True', True, 1)


# Если в функции есть например сложение, то типы данных должны совпадать

# Передача параметров по умолчанию:
def print_parms_1(a=1, b=2, c=3):
    print(a, b, c)


print_parms_1()
print_parms_1(1, c='String')  # 1-позиционный параметр, с-именованный параметр


# позиционные параметры не могут идти после именованных
# Именованные параметры можно задавать в разнобой
def print_parms_1(a=1, *, b=2, c=3):  # a -позиционный параметр, а остальные именованные
    print(a, b, c)


'''Распаковка позиционных параметров'''


def print_params(*params):  # *args **kargs
    print(*params)  # если стоит * то значения распакуются, иначе они запакованы в кортеж


print_params(1, 2, 3, 4, 5, 6, 7)


def print_parms_1(a, b, c):
    print(a, b, c)


list = [1, 2, 3]
print_parms_1(*list)

'''Именованные параметры'''
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_parms_1(**dict_)  # Занимают верное положение параметров

'''Важно!
Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же
состоянии.
def a(my_list = [])) – это приводит к ошибкам!

Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
def append_to_list(item, list_my=None):
  if list_my is None:
   list_my = []
  list_my.append(item)
print(list_my)'''

# Лекция 3
'''Произвольное число параметров'''


# Когда необходимо произвольное число параметров и мы не знаем сколько параметров будет передано
def test_funk(*params):
    print('Тип', type(params))
    print('Аргумент', params)


test_funk(1, 2, 3, 4)  # технически кортеж из параметров


def summator(txt, *values, type='sum'):  # Добавим позиционный параметр txt. Можно так же добавить именованный
    # параметр type
    s = 0
    for i in values:
        s += i
    return f'{txt}{s} {type}'


print(summator('Сумма чисел: ', 1, 2, 3, 4, type='summator'))


# Использование произвольного числа именованных параметров
def info(**values):  # При использовании ** мы сообщаем, что не знаем сколько именованных
    # параметров будет передано. Технически - это словарь
    print('Тип', type(values))
    print('Аргумент', values)
    for key, values in values.items():  # Для формирования удобочитаемого вида
        print(key, values)


# Использование произвольного числа позиционных и именованных параметров
# def info_1(*types_1, **values_1):  # При использовании ** мы сообщаем, что не знаем сколько параметров будет передано. Технически - это словарь
# Так же можно комбинировать
def info_1(value_1, *types_1, mame_1='Den', **values_1):
    print('Тип', type(values_1))
    print('Аргумент', values_1)
    for key, value in values_1.items():  # Для формирования удобочитаемого вида
        print(key, value)
    print(types_1)


info_1('Пример использования параметров всех типов', 2, 3, 4, 5, 6, names_autor='Denis', mame_1='Den',
       course='Python')


# Общая математическая функция
def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ':', s)


my_sum(1, 1, 2, 3, 4, 5)  # Сумма чисел
my_sum(2, 2, 3, 4, 5, 6, txt='Сумма квадратов')

'''Практика по функциям'''


# Максимум в списке
# Подсчёт чётных чисел в списке
# Уникальный список

def find_max(list_):  # Поиск максимального значеня
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


print(find_max([1, 2, 1, 1, 0]))


def count_event(list_):  # Подсчёт чётных чисел
    counter = 0
    for i in list_:
        if i % 2 == 0 and i != 0:
            counter += 1
    return counter


print(count_event([2, 2, 3, 4, 2, 1, 0]))


def unique(list_):  # Уникальный список
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
