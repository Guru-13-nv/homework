class Human: #Родительский класс
    head = True
    #
    # def __init__(self):
    #     self.about()

    def say_hello(self):
        print('Здравствуйте')

# class Student: #Без наследования
class Student(Human):
    head = False

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
print(student.head) #Метод about не вызывается на прямую
student.say_hello()
teacher.say_hello()