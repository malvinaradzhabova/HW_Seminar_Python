"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

name_script, product_hour, rate, bonus_at_work = argv
print("Name script: ", name_script)
print("Production in hours: ", product_hour)
print("Rate: ", rate)
print("Bonus at work: ", bonus_at_work)


salary = (int(product_hour) * int(rate)) + int(bonus_at_work)
print(f"Employee salary {salary}")


# python seminar6_hw\task1.py 200 10 10000
