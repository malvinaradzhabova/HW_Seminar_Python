"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
 нуля в качестве делителя программа должна корректно обработать эту ситуацию и
  не завершиться с ошибкой.
"""


class MyOwnError(Exception):
    def __str__(self):
        return "You can't divide by zero"


num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

try:
    num2 = int(num2)
    if num2 == 0:
        raise MyOwnError()
except ValueError:
    print("You must enter an integer to validate")
except MyOwnError as err:
    print(err)
else:
    print("Result: " + str(int(num1) / int(num2)))
