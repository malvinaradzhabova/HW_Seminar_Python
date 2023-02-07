"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
Пример:
для списка [5, "string", 0.15, True, None]
результат
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""
user_list = [5, "string", 0.15, True, None]


def list_type(_element):
    for element in range(len(user_list)):
        print(type(user_list[element]))
    return


list_type(user_list)
