def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # Ничего не возвращает
# inner_function() Вызывает ошибку
test_function()