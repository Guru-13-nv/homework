class Human:  # Родительский класс
    head = True
    _legs = True  # Делает имя только для локального использования
    __arms = True  # Делает имя ...уникальным

    #
    # def __init__(self):
    #     self.about()

    def say_hello(self):
        print('Здравствуйте')

    def about(self):
        print(self)
        print(self.head)
        print(self._legs)
        print(self.__arms)  # Имя защищено от переопределения в других классах


# class Student: #Без наследования
class Student(Human):
    # head = False
    arms = False

    def about(self):
        print('Я студент')

    # def say_hello(self):
    #     print('Здравствуйте')


class Teacher(Human):
    pass
    # def say_hello(self):
    #     print('Здравствуйте, я учитель')


# human = Human()
student = Student()
teacher = Teacher()
# print(human.head) #После наследования переменная head стала равной True
# student.about()
print(student.head)  # Метод about не вызывается на прямую
student.say_hello()
teacher.say_hello()
human = Human()
human.about()

student = Student()
student.about()

teacher = Teacher()
teacher.about()
print(dir(human))
print(student._Human__arms)  # Атрибут из класса Human
print(student.arms)  # Атрибут из класса Student
