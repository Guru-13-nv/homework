def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

tf_=test_function()
print(tf_)
if_=inner_function()
print(if_)