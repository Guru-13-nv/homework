# module_9_7
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2 == 0:
            print('Составное')
        else:
            print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
