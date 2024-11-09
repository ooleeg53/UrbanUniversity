# class Example:
#
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#
# ex = Example('data', second=25, third=3.14)

class House:  # создали класс
    houses_history = []  # атрибут, будет хранить список названий созданных объектов

    def __new__(cls, *args, **kwargs):  # переопределили метод создания объекта
        cls.houses_history.append(args[0])  # добавляем в список первое значение из позиционных аргументов
        return super().__new__(cls)  # возвращаем через функцию супер метод создания объекта из род-го класса

    def __init__(self, name, number_of_floors):  # определили метод с параметрами - имя дома, количество этажей
        self.name = name  # создали атрибут, которому присвоили передаваемое значение name
        self.number_of_floors = number_of_floors  # создали атрибут, которому присвоили передаваемое значение number_of_floors

    def go_to(self, new_floor):  # определили метод с параметром - этаж
        if new_floor > self.number_of_floors or new_floor < 1:  # определили условие, срабатывающее если параметр больше атрибута number_of_floors или меньше 1
            print('Такого этажа не существует')  # при срабатывании условия выводим сообщение
        else:  # в остальных случаях
            for i in range(1, new_floor + 1):  # для каждого значения i в диапазоне от 1 до определенного параметра
                print(i)  # выводим значение i

    def __len__(self):  # дополнили метод возвращающий длину объекта
        return self.number_of_floors  # возвращаем атрибут со значением number_of_floor

    def __str__(self):  # дополнили метод преобразующий значение в строку
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'  # возвращаем строку и атрибуты со значениями name, number_of_floor

    def __eq__(self, other):  # дополнили метод, реализующий перегрузку оператора равенства
        if isinstance(other, int):  # ставим условие если тип данных другого объекта - число
            return int(self.number_of_floors) == other  # возвращаем значение True если сравниваемые объекты равны
        elif isinstance(other, House):  # ставим еще одно условие если тип данных другого объекта - House
            return self.number_of_floors == other.number_of_floors  # возвращаем значение True если атрибуты объектов равны

    def __lt__(self, other):  # дополнили метод, реализующий перегрузку оператора меньше
        if isinstance(other, int):  # ставим условие если тип данных другого объекта - число
            return int(
                self.number_of_floors) < other  # возвращаем значение True если атрибут объекта меньше другого объекта
        elif isinstance(other, House):  # ставим еще одно условие если тип данных другого объекта - House
            return self.number_of_floors < other.number_of_floors  # возвращаем значение True если атрибут объекта self < атрибута объекта other

    def __le__(self, other):  # дополнили метод, реализующий перегрузку оператора меньше или равно
        return self.number_of_floors <= other  # возвращаем значение True если объект self <= объекта other

    def __gt__(self, other):  # дополнили метод, реализующий перегрузку оператора больше
        return self.number_of_floors > other  # возвращаем значение True если объект self > объекта other

    def __ge__(self, other):  # дополнили метод, реализующий перегрузку оператора больше или равно
        return self.number_of_floors >= other  # возвращаем значение True если объект self >= объекта other

    def __ne__(self, other):  # дополнили метод, реализующий перегрузку оператора неравенства
        return self.number_of_floors != other  # возвращаем значение True если объект self не равен объекту other

    def __add__(self, value):  # дополнили метод, складывающий объект и значение
        if isinstance(value, int):  # ставим условие если тип данных значения - число
            self.number_of_floors += value  # то плюсуем value не к объекту, а к его атрибуту number_of_floors
        return self  # возвращаем объект

    def __iadd__(self, value):  # дополнили метод - сложение с присваиванием (объект += значение)
        return self + value  # возвращаем сложенные объект и значение

    def __radd__(self, value):  # дополнили метод - отраженное сложение (значение + объект)
        return self + value  # возвращаем сложенные объект и значение

    def __del__(self): # деструктор, удаляет объект
        print(f'{self.name} снесен, но он останется в истории') # при удалении объекта, выводим сообщение


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
