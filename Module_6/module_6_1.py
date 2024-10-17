# module_6_1
# Родительские классы
class Animal:  # Класс животного
    # Атрибуты класса животного
    alive = True  # Живой.
    fed = False  # Накормленный
    name = ''  # Индивидуальное имя животного

    def __init__(self, name):  # Инициализация экземпляра класса животного
        self.name = name  # Атрибут класса животного


class Plant:  # Класс растения
    # Атрибуты класса растения
    edible = False  # Съедобный.
    name = ''  # Индивидуальное название растения

    def __init__(self, name):  # Инициализация экземпляра класса растения
        self.name = name  # Атрибут класса растения


# Дочерние классы
class Mammal(Animal):  # Класс травоядного
    # food = Plant() #Атрибут принимающий еду из класса растения
    def eat(self, food):  # Метод позволяющий животному съесть еду
        self.food = food  # Атрибут принимающий еду из класса растения
        self.fed = False  # Голодный
        if self.food.edible:  # Если еда съедобна
            self.fed = True  # Травоядное животное сыто
            print(f'{self.name} съел {self.food.name}')
        elif not self.food.edible:  # Если еда не съедобна
            Animal.alive = False  # Травоядное животное умирает
            print(f'{self.name} не стал есть {self.food.name}')


class Predator(Animal):  # Класс хищника
    # food = Plant() #Атрибут принимающий еду из класса растения
    def eat(self, food):  # Метод позволяющий животному съесть еду
        self.food = food  # Атрибут принимающий еду из класса растения
        self.fed = False  # Голодный
        if self.food.edible:  # Если еда съедобна
            self.fed = True  # Хищное животного сыто
            print(f'{self.name} съел {self.food.name}')
        elif not self.food.edible:  # Если еда не съедобна
            Animal.alive = False  # Хищное животное умирает
            print(f'{self.name} не стал есть {self.food.name}')


class Flower(Plant):  # Класс цветков
    edible = False  # Цветы не съедобны
    pass


class Fruit(Plant):  # Класс фруктов
    edible = True  # Фрукты съедобны
    pass


print(f'-------------------------\nmodule_6_1')
# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.