"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        user_list_1 = []
        for i in range(0, len(self.matrix_list)):
            user_list_2 = []
            for j in range(0, len(self.matrix_list[0])):
                user_list_2.append(
                    self.matrix_list[i][j] + other.matrix_list[i][j])
            user_list_1.append(user_list_2)
        self.matrix_list = user_list_1
        return Matrix(self.matrix_list)

    def __str__(self):
        for i in self.matrix_list:
            for j in i:
                print(j, end=" ")
            print()
        return ""


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
