# Практический пример реализации изученных конструкций
# Для проверки выйграша создадим функцию с вариантами побед:
# Из-за построчного считывания кода функции приходится
# распологать перед их использованием
from distutils.command.check import check


def check_winner():
    if (
            area[0][0] == area[0][1] == area[0][2] == 'X'
            or area[0][0] == area[1][0] == area[2][0] == 'X'
            or area[1][0] == area[1][1] == area[1][2] == 'X'
            or area[0][1] == area[1][1] == area[2][1] == 'X'
            or area[2][0] == area[2][1] == area[2][2] == 'X'
            or area[0][2] == area[1][2] == area[2][2] == 'X'
            or area[0][0] == area[1][1] == area[2][2] == 'X'
            or area[0][2] == area[1][1] == area[0][0] == 'X'
    ):
        return 'X'
    elif (
            area[0][0] == area[0][1] == area[0][2] == '0'
            or area[0][0] == area[1][0] == area[2][0] == '0'
            or area[1][0] == area[1][1] == area[1][2] == '0'
            or area[0][1] == area[1][1] == area[2][1] == '0'
            or area[2][0] == area[2][1] == area[2][2] == '0'
            or area[0][2] == area[1][2] == area[2][2] == '0'
            or area[0][0] == area[1][1] == area[2][2] == '0'
            or area[0][2] == area[1][1] == area[0][0] == '0'
    ):
        return '0'
    return '*'


# Создание игрового поля с помощью списков:
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def draw_area():
    for i in area:
        print(*i)
    print()


print('Добро пожаловать в игру')
print('-----------------------')
draw_area()
# print(area[0][0])
# area[0][0] = 'X'
for turn in range(1, 10):  # Цикл на максимальное значение игры
    print(f'Ход№: {turn}')
    if turn % 2 == 0:  # Если ход чётный и остаток от деления на 2 = 0
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1,2,3): ')) - 1
    column = int(input('Введите номер столбца (1,2,3: ')) - 1
    # Что бы взять соотвествующий элемент и поставить соответствующий знак
    # area[row][column] = 'X'
    # Что бы значения не перезаписывались и ход не тратился нужно провести проверку
    # ячейки на занятость
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ячейка занята, Вы пропускаете ход')
        draw_area()  # Что бы работала отрисовка хода
        continue
    draw_area()
    # Для проверки победителя напишем условие с использованием
    # созданной нами функции Check_winner
    if check_winner() == 'X':
        print('Победили крестики')
        break
    elif check_winner() == '0':
        print('Победа ноликов')
        break
    elif check_winner() == '*' and turn == 9:
        print('Победила дружба')