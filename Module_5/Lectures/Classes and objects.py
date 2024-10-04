# Лекция 1
class Human_1:
    # def __init__(self): # Фиксированные характеристики
    #     self.name = 'Den'
    def __init__(self, name_1):  # Принимает характеристики
        self.name_1 = name_1


# den_1 = Human_1()
# max_1 = Human_1()

# Лекция 2
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

    # Лекция3
    def __del__(self):
        print(f'{self.name_2} ушёл')

    def __len__(self):
        return self.age_2


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
print(len(den_2))  # Почему-то метод del выводит сообщение
