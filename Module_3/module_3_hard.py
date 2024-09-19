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

#Вариант решения 2
sum_result_2 = 0
def calculate_structure_sum_2(*ds_2):
    global sum_result_2
    if ds_2 != 0:
        for value_global in ds_2:
            if isinstance(value_global, str) == True:
                sum_result_2 = sum_result_2 + len(value_global)
            elif isinstance(value_global, int) == True:
                sum_result_2 = sum_result_2 + value_global
            elif isinstance(value_global, tuple) == True and value_global != 0:
                for value_internal in value_global:
                    calculate_structure_sum_2(value_internal)
            elif isinstance(value_global, list) == True  and value_global != 0:
                for value_internal in value_global:
                    calculate_structure_sum_2(value_internal)
            elif isinstance(value_global, dict) == True and value_global != 0:
                value_dict_list = list(value_global)
                for value_dict_2 in value_dict_list:
                    if isinstance(value_dict_2, dict) == True:
                        calculate_structure_sum_2(list(value_dict_2))
                    elif isinstance(value_dict_2, list) == True:
                        calculate_structure_sum_2(value_dict_2)
                    elif isinstance(value_dict_2, str) == True:
                        calculate_structure_sum_2(value_dict_2)
                        calculate_structure_sum_2(value_global[value_dict_2])
    return sum_result_2

result_2 = calculate_structure_sum_2(data_structure)
print(result_2)

a=''
b=()
c=[]
d={'cube': 7, 'drum': 8}
print(type(a),type(b),type(c),type(d))
g=list(d)
for i in g:
    print(f'key={i}, val={d[i]}')
