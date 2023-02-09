"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random

p = random.randint(0, 100)


def get_number(n):
    number = int(input("User enter number: "))
    i = 0
    if i == 10:
        print("Generated random integer = ", p)
    if number != p:
        i = n + 1
        print("Attempt № %d" % i)
    if number == p:
        print("User guess number %d" % i)
    if number > p:
        print("Generated random integer less  then yours")
        return str(get_number(i + 1))
    if number < p:
        print("Generated random integer greater than yours")
        return str(get_number(i + 1))


print(get_number(n=0))
