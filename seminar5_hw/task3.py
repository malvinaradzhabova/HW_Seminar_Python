"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""


def sum_elem(n, i=1, result=None):
    if result is None:
        result = []
    if n > 0:
        result.append(i)
        return sum_elem(n - 1, -i / 2, result)
    return result


elem = float(input("Enter the number of elements: "))
result = sum_elem(elem)
print(*result)
print(sum(result))
