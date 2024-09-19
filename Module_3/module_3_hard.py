data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_result = 0


def structure_args(*args):
    for value_1 in args:
        if isinstance(value_1, list) == True or isinstance(value_1, tuple) == True:
            structure_args(*value_1)
        elif isinstance(value_1, str) == True or isinstance(value_1, int) == True:
            calculate_structure_sum(value_1)
        elif isinstance(value_1, dict):
            structure_kwargs(**value_1)
        else:
            structure_args(*value_1)


def structure_kwargs(**kwargs):
    if isinstance(kwargs, dict) == True:
        for value_2_key in kwargs.keys():
            calculate_structure_sum(value_2_key)
        for value_2_val in kwargs.values():
            calculate_structure_sum(value_2_val)
    else:
        for i in kwargs:
            calculate_structure_sum(i)


def calculate_structure_sum(ds):
    global sum_result
    if isinstance(ds, str) == True:
        sum_result = sum_result + len(ds)
    elif isinstance(ds, int) == True:
        sum_result = sum_result + ds
    elif isinstance(ds, list) == True or isinstance(ds, tuple) == True:
        structure_args(*ds)
    elif isinstance(ds, dict) == True:
        structure_kwargs(**ds)
    return sum_result


result = calculate_structure_sum(data_structure)
print(result)

# Вариант решения 2
sum_result_2 = 0


def calculate_structure_sum_2(*ds_2):
    global sum_result_2
    for value_global in list(ds_2):
        if isinstance(value_global, str) == True:
            sum_result_2 = sum_result_2 + len(value_global)
        elif isinstance(value_global, int) == True:
            sum_result_2 = sum_result_2 + value_global
        elif isinstance(value_global, tuple) == True:
            for value_internal in list(value_global):
                calculate_structure_sum_2(value_internal)
        elif isinstance(value_global, list) == True:
            for value_internal in value_global:
                calculate_structure_sum_2(value_internal)
        elif isinstance(value_global, dict) == True:
            calculate_structure_sum_2(list(value_global.items()))
        elif isinstance(value_global, set) == True:
            for value_set in value_global:
                calculate_structure_sum_2(list(value_set))
    return sum_result_2


result_2 = calculate_structure_sum_2(data_structure)
print(result_2)

# Рекомендации преподавателя
'''1.определяем переменную которую будем использовать для суммирования результатов, например total_sum=0

2.далее arg проходимся  циклом по args (в вашем случае ds)
2.1проверяем isinstance arg на принадлежность list, tuple, set:
total_sum +=   calculate_nested_sum(*arg)
2.2 проверяем isinstance arg на принадлежность dict:
total_sum +=   calculate_nested_sum(*arg.items())
2.3 проверяем isinstance arg на принадлежность str:
total_sum +=   len(arg)
2.4 проверяем isinstance arg на принадлежность 
int,float:
total_sum += arg
2.5 если аргументов нет пасуем

3. возвращаем total_sum

4. обращаемся к функции и передаем структуру'''
sum_result_3=0
def calculate_structure_sum_3(*args_3):
    global sum_result_3
    for i_3 in args_3:
        if isinstance(i_3, list)==True or isinstance(i_3, tuple) == True or isinstance(i_3, set)==True: #[](){}
            sum_result_3 = calculate_structure_sum_3(*i_3)
        if isinstance(i_3, dict) == True: #{}
            sum_result_3 = calculate_structure_sum_3(*i_3.items())
        if isinstance(i_3, str) == True:
            sum_result_3 += len(i_3)
        if isinstance(i_3, int) == True or isinstance(i_3, float) == True:
            sum_result_3 += i_3
    return sum_result_3
result_3 = calculate_structure_sum_3(data_structure)
print(result_3)


#


a = ''
b = ()
c = []
d = {'cube': 7, 'drum': 8}
print(type(a), type(b), type(c), type(d))
g = list(d)
for i in g:
    print(f'key={i}, val={d[i]}')
