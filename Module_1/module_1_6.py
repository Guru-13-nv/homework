#module_1_6
#2.
my_dict = {'Ivan':2000}
print (my_dict) #Вывод словаря
print (my_dict['Ivan']) #Вывод значения по ключу
print (my_dict.get('member','Значение не найдено'))
my_dict.update({ #Открытие метода апдейт
    'Alex':1999
    ,'Boris':1998
}) #Добавление 2-х значений и закрытие метода
#print(my_dict)
deleted_key_1=my_dict.pop('Alex') #Присвоение объекту списка имени переменной
print(deleted_key_1)
print(my_dict)
#3.
my_set={1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1}
print(my_set)
my_set.update([152, 'Anton', True, 34.413, (10,11,1.2)])
#print(my_set) #Логический объект не добавился и ошибку не выдал, т.к. значение 1 уже присутсвует.
my_set.discard((10,11,1.2)) #удалён кортеж
print(my_set) #Вывод на экран изменённого множества