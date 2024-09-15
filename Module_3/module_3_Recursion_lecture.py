# Рекурсия
from inspect import stack


def summa(n):
    if n == 0:  # Остановка функции
        return 0
    else:
        return n + summa(n - 1)


print(summa(5))

# Стек (LIFD 'Last In First Out')
stack = []
stack.append(1)
print('Добавили элемент', stack)
stack.append(2)
print('Добавили элемент', stack)
stack.append(3)
print('Добавили элемент', stack)
print(stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
'''Когда вызываем функцию забиваем стек вызовов.
Стек вызовов - структура данных которая управляет вызовыми функций'''
