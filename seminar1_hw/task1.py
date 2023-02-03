"""
Задание 1.
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
user_name = input("Enter your name: ")
user_password = input("Enter your password: ")
user_age = int(input("Enter your age: "))
print(f"Your login details: name - {user_name}",
      f"password - {user_password}, age - {user_age}")
