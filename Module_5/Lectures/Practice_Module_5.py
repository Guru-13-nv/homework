# Практика. (Система регистрации на классах)
from random import choice


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    '''
    Класс пользователя, содержащий атрибуты: логин, пароль
    '''

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберете действие: \n 1 - Вход\n 2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    # print('ok')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        elif choice == 2:
            user = User(input('Введите логин: '), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            # := моржовый оператор
            if password != password2:
                (print('Введённые пароли не совпадают, попробуйте ещё раз'))
                continue
            database.add_user(user.username, user.password)
        #print(database.data) #Вывод словаря с логинами и паролями
