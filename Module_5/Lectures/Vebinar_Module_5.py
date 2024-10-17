from abc import ABC, abstractmethod


# Абстракция
class Publication(ABC):
    @abstractmethod
    def display(self):
        pass


# Наследники
class Book(Publication):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Book {self.title} author {self.author} year {self.year}'

    def __eq__(self, other):
        return self.year == other.year

    def __add__(self, other):
        if isinstance(other, Book) and self.author == other.author:
            return f'{self.title} and {other.title} - both written {self.author}'
        else:
            return 'The books are written by different authors'

    def display(self):
        print(str(self))# Выводим объект


class Magazine(Publication):
    # pass
    def __init__(self, title, issue, year):
        self.title = title
        self.issue = issue
        self.year = year

    def __str__(self):
        return f'Magazine {self.title} issue {self.issue} year {self.year}'

    def display(self):
        print(str(self))

# Основной класс для взаимодействия в другими классами
class Library:
    #pass
    def __init__(self):
        self.publications = [] #Инкапсуляция - закрытый объект который можно изменить только внутри класса

    def add_publ(self, publ):
        if isinstance(publ, Publication):
            self.publications.append(publ)

    def display_publ(self):
        if not self.publications:
            print('Library is empty')
        for publ in self.publications:
           publ.display()

    @property
    def last_added(self):
        if self.publications:
            print(self.publications[-1])
        return None
    @staticmethod # Статический метод. Позволяет не создавать экземпляр класса
    def count_publications(self):#, publ):
        # return len(publ.publications)
        return len(self.publications)

book_1 = Book('Clean Code', 'Robert C. Martin', 2012)
book_2 = Book('Clean Code', 'Robert C. Martin', 2017)
magaz = Magazine('Science and life', 13, 2024)

libra = Library()

libra.add_publ(book_1)
libra.add_publ(book_2)
libra.add_publ(magaz)

libra.last_added
print(libra.count_publications(libra))