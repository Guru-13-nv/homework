#module_8_1
#Задание "Программистам всё можно":
def add_everything_up(a,b):
    try:
        return round(a+b, 3)
    except TypeError:
        if (type(a) is float or type(a) is int) and type(b) is str:
            a_str = str(round(a,3))
            return a_str+b
        elif type(a) is str and (type(b) is float or type(b) is int):
            b_str = str(round(b,3))
            return a+b_str
    else:
        print('Необработанная ошибка')
    # finally:
    #     print('Программа завершена')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))