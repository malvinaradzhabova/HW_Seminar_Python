"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# Решение 1: без функции sort()
def my_func1(arg1, arg2, arg3):
    if arg1 <= arg2 and arg1 <= arg3:
        return arg2 + arg3
    elif arg2 <= arg3 and arg2 <= arg3:
        return arg1 + arg3
    else:
        return arg1 + arg2


print(my_func1(int(input("Enter argument 1: ")),
               int(input("Enter argument 2: ")),
               int(input("Enter argument 3: "))))


# Решение 2: c функцией sort()
def my_func2(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    sorted_list = (sorted(arg_list, reverse=True)[:2])
    arg_sum = sum(sorted_list)
    print(arg_sum)


print(my_func2(int(input("Enter argument 1: ")),
               int(input("Enter argument 2: ")),
               int(input("Enter argument 3: "))))
