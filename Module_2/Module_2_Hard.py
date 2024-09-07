'''Дополнительное практическое задание по модулю: "Основные операторы"
                Задание "Слишком древний шифр"'''
import random


def funk_stone():  # Функция выбора случайного камня
    stone = []  # Список значений
    for var in range(3, 21):
        stone.append(var)
    stone_random = random.choice(stone)  # Метод для рандомного выбора числа из переданного в него списка
    return stone_random

random_1 = funk_stone()
pas_final = []
for pas_1 in range(1, 20):
    for pas_2 in range(1, 20):
        if random_1 % (pas_1 + pas_2) == 0 and pas_1 < pas_2 and pas_1 != pas_2:
            pas_final.append([pas_1, pas_2])
print(f'Выпал камень: {random_1}\n Пароль к нему {pas_final}')