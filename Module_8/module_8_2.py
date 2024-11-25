# module 8.2
def personal_sum(numbers):
    incorrect_data = 0  # счетчик ошибок
    sum_values= 0  # Сумма значений в коллекции
    for number in numbers:
        try:
            sum_values+= number
        except TypeError:
            incorrect_data += 1
            print (f'Некорректный тип данных для подсчёта суммы: "{number}"')
    # print(sum_values)
    return sum_values, incorrect_data


def calculate_average(numbers):
    try:
        sum_values, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            return 0
        # print (len(numbers))
        return sum_values / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
