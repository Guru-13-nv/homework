def test_function():
    print('Функция test_function')
    def inner_function():
        print('Я в области видимости функции test_function')
    if_=inner_function()
    return if_

tf_=test_function()
print(tf_)
if_=inner_function() #Можно закомментировать, т.к. что переменная, что функция находятся в локальном пространстве имен
# функции test_function
print(if_)