class House:  # создали класс
    def __init__(self, name, number_of_floors):  # определили метод с параметрами - имя дома, количество этажей
        self.name = name  # создали атрибут, которому присвоили передаваемое значение name
        self.number_of_floors = number_of_floors  # создали атрибут, которому присвоили передаваемое значение number_of_floors

    def go_to(self, new_floor):  # определили метод с параметром - этаж
        if new_floor > self.number_of_floors or new_floor < 1:  # определили условие, срабатывающее если параметр больше атрибута number_of_floors или меньше 1
            print('Такого этажа не существует')  # при срабатывании условия выводим сообщение
        else:  # в остальных случаях
            for i in range(1, new_floor + 1):  # для каждого значения i в диапазоне от 1 до определенного параметра
                print(i)  # выводим значение i


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
