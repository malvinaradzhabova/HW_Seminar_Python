"""
Задание 2.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
number = int(input("Enter a positive integer: "))
max_number = 0
while number > 0:
    max_number = max(max_number, number % 10)
    number //= 10
print(f"The largest digit: {max_number}")
