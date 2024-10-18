# module_6_hard
'''Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными
фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного
использования таких объектов?'''
import math


class Figure:  # Родительский класс Фигуры
    sides_count = 0  # Количество сторон

    def __init__(self, color, *sides, filled=False):  # Объект создаётся с параметрами
        self.__sides = sides # Список сторон (целое число)
        self.__color = color  # Список цветов в формате RGB
        self.filled = bool(filled)  # Закрашенный (логический тип)

    def get_color(self):  # Возвращает список цветов
        '''Метод get_color, возвращает список RGB цветов.'''
        return f'Установлен цвет фигуры RGB: {self.__color}'

    def __is_valid_color(self, r, g, b):  # Проверка корректности цвета
        '''Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
        значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
        от 0 до 255 (включительно).'''
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            print(f'Некорректные значения цвета: {r}, {g}, {b}. Цвет не установлен.')

    def set_color(self, r, g, b):  # Устанавливает цвет фигуры
        '''Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.'''
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):  # Проверка корректности сторон
        '''Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все
        стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        False - во всех остальных случаях.'''
        if sides.count(self.sides_count) == 1:
            return True
        else:
            return False

    def get_sides(self):  # Возвращает список сторон
        '''Метод get_sides должен возвращать значение я атрибута __sides.'''
        return f'Стороны(а) фигуры = {self.__sides}'

    def check_class(obj, class_name):
        if isinstance(obj, class_name):
            return class_name

    def __len__(self):  # Возвращает периметр фигуры
        '''Метод __len__ должен возвращать периметр фигуры.'''
        return self.__sides[0]

    def set_sides(self, *new_sides):  # Устанавливает список сторон
        '''Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
        то не изменять, в противном случае - менять.'''
        if new_sides.count(self.sides_count) == 1:
            print(f'Стороны фигуры не изменились')
        else:
            self.__sides = list(new_sides)
            print(f'Стороны фигуры изменились на: {self.__sides}')
            return self.__sides

    # pass


class Circle(Figure):  # Круг
    '''Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
'''
    sides_count = 1  # Количество сторон
    circle_area = 0  # Площадь круга

    def __init__(self, color, sides):
        self.sides = int(sides)  # Количество сторон
        super().__init__(color, sides, filled=False)
        self.__radius = int(sides // 2 * 3.14)  # Радиус фигуры

    def get_square(self):  # Возвращает площадь фигуры
        self.circle_area = self.__radius ** 2 * 3.14  # Площадь круга
        return int(self.circle_area)


class Triangle(Figure):  # Треугольник
    '''Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)'''
    sides_count = 3  # Количество сторон
    triangle_area = 0  # Площадь треугольника

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=False)

    def get_square(self):  # Возвращает площадь фигуры
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = 0.5 * (a + b + c)
        self.triangle_area = math.sqrt(p(p - a)(p - b)(p - c)) # Для этой операции импортируем библиотеку математика
        return int(self.triangle_area)

    # pass


class Cube(Figure):
    '''Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.'''
    sides_count = 12  # Количество сторон
    sides_list = []  # Список сторон
    V_cube = 0  # Объём куба

    def __init__(self, color, *sides):
        for i in range(self.sides_count): # Составляем список сторон
            self.sides_list.append(sides[0])
        sides = self.sides_list # Список сторон для передачи в родительский класс
        super().__init__(color, *sides, filled=False)

    def get_volume(self):
        '''Метод get_volume, возвращает объём куба.'''
        # По скольку у куба стороны равны, а список сторон хранится в sides_list
        a = self.sides_list[0] # Первая сторона
        b = self.sides_list[1] # Вторая сторона
        c = self.sides_list[2] # Третья сторона
        self.V_cube = a * b * c # Объём куба
        return f'Объём куба = {self.V_cube}'
    # pass


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
