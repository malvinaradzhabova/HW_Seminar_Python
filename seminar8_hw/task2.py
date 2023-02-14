"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


user_file = open("example_2.txt", "r")
content = user_file.read()
print(f"File contents: \n {content}")
user_file = open("example_2.txt", "r")
content = user_file.readlines()
print(f"Number of lines in file: {len(content)}")
user_file = open("example_2.txt", "r")
content = user_file.readlines()
for i in range(len(content)):
    print(f"Number of words {i + 1}  in each line {len(content[i])}")
user_file = open("example_2.txt", "r")
content = user_file.read()
content = content.split()
print(f"Total number of words: {len(content)}")
user_file.close()
