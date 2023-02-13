"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие
публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} rides"

    def stop(self):
        return f"{self.name} stopped"

    def turn_right(self):
        return f"{self.name} turned right"

    def turn_left(self):
        return f"{self.name} turned left"

    def show_speed(self):
        return f"Current speed {self.name} is {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of town car {self.name} is {self.speed}")

        if self.speed > 60:
            return f"Attention!!!Speed of {self.name} " \
                   f"is higher than allow for town car"
        else:
            return f"Speed of {self.name} is normal."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of work car {self.name} is {self.speed}")

        if self.speed > 40:
            return f"Attention!!!Speed of {self.name} is higher " \
                   f"than allow for work car"
        else:
            return f"Speed of {self.name} is normal."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} is real police car"
        else:
            return f"{self.name} is not police car"


BMWi8 = SportCar(240, "Grey", "BMWi8", False)
Mazda = TownCar(50, "Black", "Mazda", False)
Komatsu = WorkCar(80, "Yellow", "Komatsu", False)
Lada = PoliceCar(90, "Grey", "Lada", True)
print(BMWi8.turn_right())
print(BMWi8.show_speed())
print(Mazda.show_speed())
print(Lada.police())
print(Komatsu.show_speed())
print(f"{Komatsu.name} is {Komatsu.color}")
print(f"Is {Komatsu.name} a police car? {Komatsu.is_police}")
print(f"When the red light came on {Mazda.go()}, {Lada.turn_right()} "
      f"and {BMWi8.stop()} ")
print(Komatsu.turn_left())
print(f"Is {Lada.name}  a police car? {Lada.is_police}")
