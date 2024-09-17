# module_3_5


def get_multiplied_digits(number):
    str_number = str(number)
    len_str_number = len(str_number)-1
    first = int(str_number[0])
    # if len(str_number) == 1:
    #     return first
    if int(str_number[-1]) != 0 and len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif int(str_number[-1]) == 0 and len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:len_str_number:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(0)
print(result)

result = get_multiplied_digits(240)
print(result)