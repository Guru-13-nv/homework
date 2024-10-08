# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от
# значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).
# Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
# Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне от 2 до этого числа(не включительно).
# Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель. (Не обязательно)
# Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime, в кругах разработчиков называются перменными-флагами(flag).


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Дан список
primes = []  # Обявляем глобальную переменную, т.к. переменные цикла или условия живут в рамках цикла или условия
not_primes = []
# print (len(numbers))
for value_1 in numbers:  # Обозначаем набор значений, где value_1 поочерёдно принимает значения списка
    if value_1 == 1:  # Отсеиваем 1, что бы она не участвовала в проверке и на неё не тратить итерацию последующего цикла
        continue
    is_prime = True  # Флаг на простоту числа. Все перебираемые значения получают признак верных.
    for value_2 in range(2, value_1 - 1):  # Выставляем, что бы перебор шёл сугубо до указанного по индексу числа.
        # Значение value_2 принимает значение списка -1 и начинается с 2
        # Описание фильтров
        if value_1 % value_2 == 0 and value_1 != 1:  # Так как список верный, что проходит по фильтру ставим признак Лож
            # т.е. если число делится на что-то ещё кроме себя и 1, оно получает признак натуральности - Лож
            is_prime = False  # Признак выставляется если наёден делитель в промежутке между 1 и до самого число (не включительно)
            break  # Как только делитель найден цикл прекращается и начинается проверка следующего числа
    if is_prime == True:  # Те числа которые в первом цикле получили значение Правда добавляются в список
        primes.append(value_1)
    elif is_prime == False:  # Те числа в рамках первого цикла получили значение Лож добавляются в список
        not_primes.append(value_1)
print(f'Простые числа: {primes}\nСоставные числа: {not_primes}')
