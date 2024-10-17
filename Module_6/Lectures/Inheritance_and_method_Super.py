class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group) # Вызов конструктора класса Group
        super().about()

    def info(self):
        print(f"My name is {self.name}")


class Student_Group:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, Student_Group): # Используем множественное наследование
    def __init__(self, name, place, group):
        # Human.__init__(self, name) #Обращаемся к родительскому классу по имени
        super().__init__(name, group)  # Обращаемся к родительскому классу
        self.place = place
        super().info()


# human1 = Human("John")
# print(human1.name)
student1 = Student("John", "Urban", 'Python_1')
# print(student1.name)
# Student.Student_Group.about(student1)
print(Human.mro()) #Цепочка наследования
print(Student.mro()) #Цепочка наследования
