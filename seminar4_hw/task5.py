"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""
# Возьмем для примера задачу № 4. C помощью модуля timeit
# замерим время выполнения данного кода

from timeit import timeit


def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
        if y >= 0:
            return res
        else:
            return 1 / res


print(my_func(int(input("Enter a positive number x: ")),
              int(input("Enter a negative number y: "))))
print(timeit("my_func", globals=globals(), number=10000))


#  0.00013139995280653238. Оптимизирую код

def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(int(input("Enter a positive number x: ")),
              int(input("Enter a negative number y: "))))
print(timeit("my_func", globals=globals(), number=10000))

#  0.00011979998089373112.
# Таким образом, производительность кода увеличилась на 8,83%
