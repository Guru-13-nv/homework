# module 9_2
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']  # Список имён, состоящий из строк
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']  # Второй список, состоящий из слов

first_result = [len(i) for i in first_strings if len(i) >= 5]  # Список длин строк
second_result = [(i, j) for i in first_strings for j in second_strings if
                 len(i) == len(j)]  # Список пар слов одинаковой длины
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}  # Словарь циклических сравнений

print(first_result)
print(second_result)
print(third_result)
