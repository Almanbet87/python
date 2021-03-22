# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"The {self.name}'s gone"

    def stop(self):
        return f"\nThe {self.name} stopped"

    def turn_right(self):
        return f"\nThe {self.name} is turned right"

    def turn_left(self):
        return f"\nThe {self.name} is turned left"

    def show_speed(self):
        return f"\nCurrent speed is {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nSpeed over 40 km/h is not allowed for this area'
        else:
            return f'The speed is acceptable for this area'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nSpeed over 60 km/h is not allowed for this area'
        else:
            return f'The speed is acceptable for this area'


class PoliceCar(Car):
    pass


town = TownCar(70, 'white', 'Mercedec',  False)
print('1:\n' + town.go(), town.show_speed(), town.turn_left(), town.turn_right(), town.stop())

sport = SportCar(170, 'red', 'Lamborgini', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn_left(), sport.stop())

work = WorkCar(30, 'blue', 'Skoda', False)
print('3:\n' + work.go(), work.show_speed(), work.turn_left(), work.stop())

police = PoliceCar(100, 'black', 'Lada', True)
print('4:\n' + work.go(), work.show_speed(), work.turn_left(), work.stop())
