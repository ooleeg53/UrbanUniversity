def get_matrix(n, m, value): #объявили функцию с параметрами
    matrix = [] # создали пустой список
    for i in range(n): # создали цикл для перебора кол-ва строк (n)
        matrix.append([]) # добавили новый список для каждой 'i' в диапазоне(n)
        for k in range(m): # создали внутренний цикл для перебора кол-ва столбцов (m)
            matrix[i].append(value) # добавляем в список[i] значение (value) для каждой 'k' в диапазоне(m)
    return matrix # возвращаем значение списка matrix из функции

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
