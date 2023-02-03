"""
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time = int(input("Enter time in seconds: "))
hour = time // 3600
minute = time // 60
second = (hour * 3600 + minute * 60) - time
print(f"Time in hh:mm:ss: format {float(hour)} : {float(minute)} : {second}")