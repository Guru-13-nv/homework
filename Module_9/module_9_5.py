# module_9_5
class StepValueError(ValueError):  # Задаём класс StepValueError
    pass


class Iterator:  # Задаём класс Iterator
    def __init__(self, start, stop, step=1):  # Задаём конструктор объектов класса
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):  # Задаём метод __iter__
        self.pointer = self.start
        return self

    def __next__(self):  # Задаём метод __next__
        if self.step > 0 and self.pointer > self.stop:  # Если шаг больше нуля и указанный указатель больше или равен указателя стоп, то выходим из цикла
            raise StopIteration  # Выходим из цикла
        elif self.step < 0 and self.pointer < self.stop:  # Если шаг меньше нуля и указанный указатель меньше или указателя стоп, то выходим из цикла
            raise StopIteration  # Выходим из цикла
        else:
            current = self.pointer
            self.pointer += self.step  # Иначе увеличиваем указатель на шаг
            return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
