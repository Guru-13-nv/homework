'''Задача "Однокоренные":
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее
неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или
наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.'''


def single_root_words(root_word, *other_words):
    same_words = []
    other_words_lower = []
    for value_1 in other_words:
        other_words_lower.append(value_1.lower())
        value_lower = value_1.lower()
        root_word_lower = root_word.lower()
        # if str(root_word_lower) in other_words_lower or root_word_lower.find(value_lower) > -1:
        #     same_words.append(value_1) # Долго не мог сообразить, почему не выводит, а потом понял, что эл-та в спске
        # нет а только часть элемента
        if value_lower.find(root_word) > -1 or root_word_lower.find(value_lower) > -1:
            same_words.append(value_1)
    return same_words


# a='urban.fan@mail.ru'
# b=['@', '.com', '.ru', '.net']
# for c in b:#Цикл с использованием метода сравнения строк
#     d=a.find(c)
#     print(d)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
