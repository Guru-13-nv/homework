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

a = []
b = ()
c = {}
d = 'a'
g = 4
print(f'a={type(a)}, b={type(b)}, c={type(c)}, d={type(d)}, g={type(g)}')
isinstance(a, list)
e = {'cube': 7, 'drum': 8}
print(list(e))
print(e.values())
for i in e.values():
    print(isinstance(i, int))
print(e.keys())
print(len(d))
print(list(data_structure))

for i in list(data_structure):
    print(i)
    print (type(i))
    for j in i:
        print(j)
        print(type(j))
