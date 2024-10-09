# Лекция 1 (Классы и объекты)
class Human_1:
    # def __init__(self): # Фиксированные характеристики
    #     self.name = 'Den'
    def __init__(self, name_1):  # Принимает характеристики
        self.name_1 = name_1


# den_1 = Human_1()
# max_1 = Human_1()

# Лекция 2 (Атрибуты и методы объекта. Указатель на свой объект в методах)
class Human_2:
    def __init__(self, name_2, age_2):  # Принимает характеристики
        self.name_2 = name_2
        self.age_2 = age_2

    # Методы
    def say_info_2(self):
        print(f'Привет, меня зовут {self.name_2}, мне {self.age_2}')

    def birthday_2(self):
        self.age_2 += 1
        print(f'У меня сегодня день рождения мне сегодня {self.age_2}')

    # Лекция3 (Специальные методы классов)
    def __del__(self):
        print(f'{self.name_2} ушёл')

    def __len__(self):
        return self.age_2

    # Лекция 4 (Специальные методы классов)
    def __lt__(self, other):  # lover than
        return self.age_2 < other.age_2

    def __gt__(self, other):  # greater than
        return self.age_2 > other.age_2

    def __eq__(self, other):
        return self.name_2 == other.name_2 and self.age_2 == other.age_2

    def __bool__(self):  # Если не = 0, то истина
        return bool(self.age_2)
    def __str__(self): #Строковое представление объекта
        return f'{self.name_2}'


den_2 = Human_2('Денис', 22)
max_2 = Human_2('Макс', 22)
print(den_2.name_2, den_2.age_2)
print(max_2.name_2, max_2.age_2)
den_2.age_2 = 23
print(den_2.name_2, den_2.age_2)
den_2.say_info_2()
max_2.say_info_2()
max_2.birthday_2()
# del den_2 # Диструктор
# max_2.birthday_2()
# input() # После ввода значения будет удалён и Макс
# Лекция 3
print(len(den_2))  # Почему-то метод del выводит сообщение
# Лекция 4
print(den_2 < max_2)
print(max_2 == den_2)
print(max_2)
