'''Дополнительное практическое задание по модулю: "Основные операторы"
                Задание "Слишком древний шифр"'''
import random


def funk_stone():  # Функция выбора случайного камня
    stone = []  # Список значений
    for var in range(3, 21):
        stone.append(var)
    stone_random = random.choice(stone)  # Метод для рандомного выбора числа из переданного в него списка
    # print(stone)
    # print(stone_random)
    return stone_random


# print(funk_stone())

random_1 = funk_stone()
pas_final = []
# for pas_1 in range(random_1, 21):
for pas_2 in range(1, 20):
    for pas_3 in range(1, 20):
        #sum_1 = pas_2 + pas_3
        # mult_1 = random_1 % sum_1
        if random_1 % (pas_2 + pas_3) == 0 and pas_2 < pas_3 and pas_2 != pas_3:
            pas_final.append([pas_2, pas_3])
            #break
        # print(pas_final)
    # print(f'Число -{random_1}- Цикл -{pas_2}- Сумма -{sum_1}- Кратность -{random_1%sum_1}')
    # print(f'Сумма -{sum_1}- sum_1')
    # print(f'Кратность -{mult_1}- mult_1')
    # print(f'рандом -{pas_1}- pas_1')
print(f'Выпал камень: {random_1}\n Пароль к нему {pas_final}')
