"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


user_file = open("example.txt", "w")
line = input("Enter text: \n")
while line:
    user_file.writelines(line)
    line = input("Enter text: \n")
    if not line:
        break

user_file.close()
user_file = open("example.txt", "r")
content = user_file.readline()
print(content)
user_file.close()
