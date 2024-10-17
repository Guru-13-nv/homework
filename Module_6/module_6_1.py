# module_6_1
#Родительские классы
class Animal: # Класс животного
    #Атрибуты класса животного
    alive = True #Живой.
    fed = False #Накормленный
    name = '' #Индивидуальное имя животного
    def __init__(self, name):
        self.name = name
        # self.alive = alive
        # self.fed = fed
    # pass

class Plant: # Класс растения
    #Атрибуты класса растения
    edible = False #Съедобный.
    name = '' #Индивидуальное название растения
    def __init__(self, name):
        self.name = name
        # self.edible = edible
    # pass

# Дочерние классы
class Mammal(Animal): #Класс травоядного
    #food = Plant() #Атрибут принимающий еду из класса растения
    def eat(self, food): #Метод позволяющий животному съесть еду
        self.food = food
        self.fed = False
        if self.food.edible:
            self.fed = True
            print(f'{self.name} съел {self.food.name}')
        elif not self.food.edible:
            Animal.alive = False
            print(f'{self.name} не стал есть {self.food.name}')
    # pass

class Predator(Animal): #Класс хищника
    #food = Plant() #Атрибут принимающий еду из класса растения
    def eat(self, food): #Метод позволяющий животному съесть еду
        self.food = food
        self.fed = False
        if self.food.edible:
            self.fed = True
            print(f'{self.name} съел {self.food.name}')
        elif not self.food.edible:
            Animal.alive = False
            print(f'{self.name} не стал есть {self.food.name}')
    #pass

class Flower(Plant): #Класс цветков
    edible = False
    pass

class Fruit(Plant): #Класс фруктов
    edible = True
    pass

print(f'-------------------------\nmodule_6_1')
#Выполняемый код(для проверки):
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