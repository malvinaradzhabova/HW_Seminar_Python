"""
Задача 1.
 Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

season_dict = {
    "winter": ["1", "2", "12"],
    "spring": ["3", "4", "5"],
    "summer": ["6", "7", "8"],
    "autumn": ["9", "10", "11"]
}
season_list = [
    ["winter", ["1", "2", "12"]],
    ["spring", ["3", "4", "5"]],
    ["summer", ["6", "7", "8"]],
    ["autumn", ["9", "10", "11"]]
]
while True:
    number = input("User enter month number: ")
    if number not in sum(season_dict.values(), []):
        print("Mistake")
        continue

    break

for season, month in season_list:
    if number in month:
        print(f"Result through list: {season}")
for season, month in season_dict.items():
    if number in month:
        print(f"Result through dictionary: {season}")
