# module_7_2
# Задача "Записать и запомнить":
def custom_write(file_name, strings):  # функция записи в файл
    """Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для
    записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью."""
    strings_positions = {}  # Словарь с ключами (<номер строки>, <байт начала строки>)
    file_note = open(file_name, 'w', encoding='utf-8')  # Создаём файл для записи
    for key, entry in enumerate(strings, start = 1):# Записываем в файл все строки из списка strings с номером key
        bytes_start = file_note.tell() # Положение курсора перед записью
        file_note.write(entry + '\n') # Формирование текстовой строки и перевод курсора на следующую строку
        tuple_number = (key, bytes_start) # Создаём кортеж
        strings_positions [tuple_number] = entry  # Заносим в словарь
    file_note.close()  # Закрываем файл
    return strings_positions  # Возвращаем словарь

# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
