# module_9_6
# Для функции генератора используйте оператор yield.
def all_variants(text):  # цикл для всех вариантов
    for i in range(len(text)):  # для каждого символа
        yield text[i:i + 1]
    for i in range(len(text)):  # для пар символов
        yield text[i:i + 2]
        if i == 1:
            break
    yield text  # для группы символов


a = all_variants("abc")
for i in a:
    print(i)
