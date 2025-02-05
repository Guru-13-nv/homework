# module 9_3
first = ['Strings', 'Student', 'Computers'] #Сптроки из списка first
second = ['Строка', 'Урбан', 'Компьютер'] #Сптроки из списка second

first_result = [len(f) - len(s) for f, s in zip(first, second) if len(f) - len(s) != 0] #Генераторная сборка первого списка с исполнением функции zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first))) #Генераторная сборка второго списка с исполнением range и len

print(list(first_result))
print(list(second_result))