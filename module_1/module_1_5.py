#module_1_5
immutable_var=tuple([1,2,3,4,'Urban',True])
print(immutable_var)
#print(immutable_var[1])
#immutable_var[1] = 4
#print(immutable_var[1]) #TypeError: объект 'tuple' не поддерживает назначение элементов
#Объекты картежа являются не изменяемыми, если объектом не является список.
mutable_list=['Milk', 1, True]
#print (type (mutable_list))
print (mutable_list)
mutable_list[0]='banana'
mutable_list[1]=100
mutable_list[2]=False
print (mutable_list)