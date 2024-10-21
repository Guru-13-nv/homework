# module_7_3
#Задача "Найдёт везде":
import string


class WordsFinder:
    file_names = [] # список файлов
    def __init__(self, *files):
        for name in files: # Цикл по переданным именам файлов
            self.file_names.append(name)# добавляем в список переданные имена файлов
            file = open(name, 'w', encoding='utf-8') # Макет наполнения файла
            file.write("It's a text for task Найти везде\n"
                       "Используйте его для самопроверки\n"
                       "Успехов в решении задачи!\n"
                       "text text text\n")  # Запись в файл. Перезаписывает файл
            file.close()

    def get_all_words(self): # Получить все слова
        '''Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.'''
        all_words = {} # словарь файлов и их слов
        for file in self.file_names: # Цикл по списку файлов
            with open(file, 'r', encoding='utf-8') as name_file: # открываем файл
                file_str = name_file.read() # читаем весь файл построчно, поэтому не используем цикл
                file_str_lo = file_str.lower() # переводим строку в нижний регистр
                str_pynct = file_str_lo.translate(str.maketrans('', '', string.punctuation)) # удаляем пунктуацию
                # используя метод translate из библиотеки string
                list_word = str_pynct.split() # переводим строку в список слов разбивая по пробелу
                all_words[file] = list_word # добавляем слова в словарь
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items(): # Цикл по словарю где name- название файла, words - список слов
            if word.lower() in words: # Вхождение слова в словарь
                output = words.index(word.lower()) + 1 # Индекс первого вхождения слова + 1, т.к. индекс начинается с нуля
        return f'В файле {name} найдено слово {word} на позиции {output}'

    def count(self, word):
        for name, words in self.get_all_words().items(): # Цикл по словарю где name- название файла, words - список слов
            count = 0 # Объявление счётчика
            for word_search in words: # Перебор слов из списка
                if word.lower() == word_search: # Совпадающие слова
                    count += 1 # Увеличиваем счётчик
        return f'Всего найдено {count} слов {word}'


#Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего