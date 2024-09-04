# Цель: применить навыки создания цикла while, а так же применения операторов break и continue.
#
# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не
# закончится список (выход за границу).
#
# Пункты задачи:
# Запишите исходный список в переменную my_list.
# Напишите цикл while с соответствующими задаче условиями.
# Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.
from itertools import count

list_number = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
# print (len(list_number))
# print (list_number [1])
while number <= len(list_number) - 1:  # Ограничение цикла, нумерация индексов начинается с нуля.
    if list_number[number] > 0:  # Условие цикла, где 0 - не является положительным и не является отрицательным числом
        print(list_number[number])
        number = number + 1
    elif list_number[number] == 0: #Поскольку ноль не останавливает цикл и не выводится
        number = number + 1
    else:
        print('Список закончился или найдено отрицательное число')
        break  # Остановка цикла при неудовлетворении условиям
# Если выписать просто все положительные числа
# while number <= len(list_number)-1:
#     if list_number[number] > 0:
#         print(list_number[number])
#         number = number + 1
#     else:
#         number = number + 1
#         continue