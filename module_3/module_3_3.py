def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b='строка_строка')  # меняем один именованный параметр, остальные неизменны
print_params(a=123, c=False)  # меняем два именованных параметра, один неизменный
print_params(a=543, b='param pam pam', c=False)  # меняем все именованные параметры
print_params()
print_params(b=25)  # вызов работает, но ругается на разный тип данных
print_params(c=[1, 2, 3])  # вызов работает, но ругается на разный тип данных

values_list = [77, 'привет пока', True]
values_dict = {'a': 2, 'b': 'точка', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [66, 'hello bye']
print_params(*values_list_2, 42)  # работает


# Важно!
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!

# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)


append_to_list(1, ['hi', 3, 2])
