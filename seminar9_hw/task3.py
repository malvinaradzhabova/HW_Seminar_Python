"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у
 пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class CheckNumber(ValueError):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    try:
        value = input("Enter number: ")
        if value == "cancel":
            break
        if not value.isdigit():
            raise CheckNumber(value)
        user_list.append(int(value))
    except CheckNumber as ex:
        print("Mistake!It is not a number")
print(user_list)
