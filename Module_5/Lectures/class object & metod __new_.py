class User:
    __instance = None

    def __new__(cls, *args, **kwargs):  # Переопределение класса
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        # self.kwargs = kwargs
        for key, values in kwargs.items():
            setattr(self, key, values)


other_ = [1, 2, 3]
user_ = {'name': 'Den', 'age': 25, 'gender':'male'}

# user1 = User(other_, user_, name='Den')
user1 = User(*other_, **user_)
# user2 = User()
# print(User.__mro__)
# print(user1 is user2)
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)
