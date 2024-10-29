import random


def first_area(): # создаем функцию, где числа от 3 до 20 выводятся рандомно
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    global number # присваиваем переменной глобальное значение, чтоб к ней можно было обращаться вне функции
    number = random.choice(numbers)
    print('Число: ', number)


first_area()


def second_area(): # создаем функцию, где записываются те пары чисел, сумма которых кратна числу из first_area
    s_area = [] # создаем список, куда будем вписывать парные числа
    for i in range(1, 21):
        for k in range(1, 21):
            if number % (i + k) == 0 and i != k and i <= k: # условия при которых числа будут записываться в список
                s_area.append(i)
                s_area.append(k)

    print('Пароль:', *s_area)


second_area()
