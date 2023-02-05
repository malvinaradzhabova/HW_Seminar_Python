"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def func(number_1, number_2):
    try:
        quotient = number_1 / number_2
    except ZeroDivisionError:
        return "Are you sure? Don't try to divide by 0!"
    except ValueError:
        return "Enter natural number"
    return quotient


print(func(int(input("Enter number 1: ")), int(input("Enter number 2: "))))
