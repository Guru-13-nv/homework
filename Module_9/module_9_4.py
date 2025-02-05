# module_9_4
first = 'Мама мыла раму'
second = 'Рамена мало было'

list_test = list(
    map(lambda first, second: first in second, first, second))  # Лямдбда-функция сравнивает символы в строках
print(list_test)


def get_advanced_writer(file_name):  # Функция для cоздания файла
    def write_everything(*data_set):  # Функция для записи в файл
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])  # Записывает данные в файл в таком виде

from random import choice


class MysticBall:  # Класс для случайного выбора слов
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


firs = MysticBall('Да', 'Нет', 'Наверное')
print(firs())
print(firs())
print(firs())
