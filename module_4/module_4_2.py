
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() # при запуске ничего не произойдет
# inner_function() # выдаст ошибку, поскольку эта функция не определена вне функции test_function
test_function() # выдаст сообщение из внутренней функции inner_function

