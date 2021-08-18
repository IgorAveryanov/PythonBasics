# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{self.speed}, {self.color}, {self.name}, {self.is_police}')

    def go(self):
        print(f'{self.name} is moving!')

    def stop(self):
        print(f'{self.name} has stopped!')

    def turn(self, direction):
        print(f'{self.name} turned {direction}!')

    def show_speed(self):
        print(f'Current speed: {self.speed}')

    def is_police_check(self):
        if self.is_police:
            print(f'{self.name} is a police car')
        else:
            print(f'{self.name} is NOT a police car')


class TownCar(Car):

    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.name} current speed: {self.speed}')
        else:
            print(f'{self.name} is exceeding the speed limit!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed <= 40:
            print(f'{self.name} current speed: {self.speed}')
        else:
            print(f'{self.name} is exceeding the speed limit!')


class PoliceCar(Car):
    pass


# TownCar class object example       
BMW = TownCar(70, 'black', 'X5', False)
print(BMW.__class__.__name__)
BMW.go()
BMW.stop()
BMW.turn('right')
BMW.show_speed()
BMW.is_police_check()

print()

# SportCar class object example 
Ferrari = SportCar(120, 'red', 'F40', False)
print(Ferrari.__class__.__name__)
Ferrari.go()
Ferrari.stop()
Ferrari.turn('upside-down')
Ferrari.show_speed()
Ferrari.is_police_check()

print()

# WorkCar class object example
Skoda = WorkCar(41, 'green', 'Fabia', False)
print(Skoda.__class__.__name__)
Skoda.go()
Skoda.stop()
Skoda.turn('left')
Skoda.show_speed()
Skoda.is_police_check()

print()

# PoliceCar class object example
Chevrolet = PoliceCar(80, 'white', 'Camaro', True)
print(Chevrolet.__class__.__name__)
Chevrolet.go()
Chevrolet.stop()
Chevrolet.turn('backward')
Chevrolet.show_speed()
Chevrolet.is_police_check()
