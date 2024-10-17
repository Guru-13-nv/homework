# module_6_2
class Vehicle:  # Класс автомобилей
    # owner = str('')  # Владелец
    # __model = str('')  # Модель
    # __engine_power = int(0)  # Мощность двигателя
    # __color = str('')  # Цвет
    __color_variant = ['blue', 'red', 'green', 'black', 'white']  # Варианты цветов

    def __init__(self, owner, model, color, engine_power):  # Конструктор
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):  # Возвращает модель автомобиля
        return f'Модель: {self.__model}'

    def get_horsepower(self):  # Возвращает мощность двигателя
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):  # Возвращает цвет автомобиля
        return f'Цвет: {self.__color}'

    def print_info(self):  # Выводит информацию о автомобиле
        print(
            f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\n'
            f'Цвет: {self.__color}\nВладелец: {self.owner}'
        )

    def set_color(self, new_color):  # Выбирает цвет автомобиля из списка
        if new_color.lower() in self.__color_variant:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    pass


class Sedan(Vehicle):
    # def get_model(self): # Возвращает модель автомобиля
    #     return f'Модель: {self.__model}'
    # def get_horsepower(self): # Возвращает мощность двигателя
    #     return f'Мощность двигателя: {self.__engine_power}'
    # def get_color(self): # Возвращает цвет автомобиля
    #     return f'Цвет: {self.__color}'
    # def print_info(self): # распечатывает результаты методов (в том же порядке)
    #     print(
    #         f'Модель: {self.__model}, Мощность двигателя: {self.__engine_power}'
    #         f', Цвет: {self.__color}\n Владелец: {self.owner}'
    #     )
    # def set_color(self, new_color): # Выбирает цвет автомобиля из списка
    #     new_color = str(new_color)
    #     if new_color.lower() in (color.lower() for color in self.__color_variant):
    #         self.__color = new_color
    #     else:
    #         print(f'Нельзя сменить цвет на {new_color}')
    __passenger_limit = 5  # Максимальное кол-во пассажиров
    pass


# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
