#module_1_4
my_string = input ('Введите название университета: ')
print ('Количество символов введёного текста:otus.ru',len (my_string))
#print (type(my_string))
print (my_string.upper()) #Верхний регистр
print (my_string.lower()) #Нижний регистр
print (my_string.replace(' ','')) #Удаление пробелов. Теги _old и _new - не понятны, подставились сами при вводе значений
print (my_string[0]) #Вывод первого символа
print(my_string[-1]) #Вывод последнего символа