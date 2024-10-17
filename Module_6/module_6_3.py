# module_6_3
# Задача "Мифическое наследование":
class Horse:  # класс Horse
    x_distance = 0  # Атрибут пройденный путь
    sound = 'Frr'  # Звук который издаёт

    def run(self, dx): # Метод пройденный путь
        self.x_distance += dx # Добавляем к атрибуту пройденный путь


class Eagle:  # Создание класса Eagle
    y_distance = 0  # Высота полёта
    sound = 'I train, eat, sleep, and repeat' #  звук, который издаёт орёл (отсылка)

    def fly(self, dy): # Увеличение высоты полёта
        self.y_distance += dy

class Pegasus (Horse, Eagle): # Создание класса Pegasus
    def move(self, dx, dy): # Метод пройденный путь и высота полёта
        super().run(dx) # Вызываем метод пройденный путь с помощью метода super()
        super().fly(dy) # Вызываем метод высоты полёта с помощью метода super()

    def get_pos(self): # Метод возвращающий позицию
        return (self.x_distance, self.y_distance) # Возвращаем позицию объекта, а не метод

    def voice(self):# Метод, который выводит звук
        print(Eagle.sound) # Выводим звук орла, обращаясь к атрибуту класса Eagle

#Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()