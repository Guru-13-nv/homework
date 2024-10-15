# Задача "Developer - не только разработчик":
class House:

    houses_history = []  # module_5_4

    # module_5_4
    def __new__(cls, *name, **number_of_floors):
        if name[0] not in cls.houses_history:
            cls.houses_history.append(name[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    # module_5_2
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {str(self.name)}, количество этажей: {str(self.number_of_floors)}'

    # module_5_3
    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Сравнить можно только объекты одного типа lt')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Сравнить можно только объекты одного типа le')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Сравнить можно только объекты одного типа gt')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Сравнить можно только объекты одного типа ge')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Сравнить можно только объекты одного типа')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return House(self.name, self.number_of_floors)

    def __radd__(self, value):
        if isinstance(value, int):
            House.__add__(self, value)
            return House(self.name, self.number_of_floors)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return House(self.name, self.number_of_floors)
#module_5_4.py
    def __del__(self):
        print(f'{str(self.name)} снесён, но он останется в истории')


print('--module_5_1--')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print('-----------------------------------------')
print('--module_5_2--')
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
print('-----------------------------------------')
print('--module_5_3--')
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

# print(type(h1))
# print(type(h2))

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print('-----------------------------------------')
print('--module_5_4--')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
