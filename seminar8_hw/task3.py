"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

user_file = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("example_3.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        for key in user_file.keys():
            line = line.replace(key, user_file[key])
        print(line)
        with open("example_4.txt", "a", encoding="utf-8") as file_translate:
            file_translate.write(f"\n {line}")
