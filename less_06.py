#1
import time

class TrafficLight:
    _color = ['красный', 'желтый', 'зеленый']

    def running(self):
        time_pause = [7, 2, 7]
        for i in range(0, 3):
            print(TrafficLight._color[i])
            time.sleep(time_pause[i])

TrLi_1 = TrafficLight()
TrLi_1.running()

#2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        weight = 25
        height = 5
        mass = int(self._width) * int(self._length) * weight * height
        print(f'Для дороги длиной {self._length} м и шириной {self._width}м масса асфальта составит {mass} кг')

road1 = Road(100, 50)

#3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        _income = {'wage': wage, 'bonus': bonus}
        self._income = _income

class Position(Worker):
   def get_full_n(self):
        print(f'имя {self.name} фамилия {self.surname} в должности {self.position}')

   def get_total_income(self):
        total_income =self._income['wage'] * self._income['bonus']
        return total_income

woker1 = Position('Олег', 'Иванов', 'инженер', 30, 50)
woker1.get_full_n()
print(f'получает {woker1.get_total_income()} $')

#4
class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = bool(is_polise)

    def go(self):
        info = 'car has started'
        return info

    def stop(self):
        info2 = 'car has stopped'
        return info2

    def turn(self, direction):
        info3 = f'car has turned {direction}'
        return info3

    def show_speed(self):
        info4 = f'speed now {self.speed}'
        return info4

class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            return f'speed now -{self.speed}'
        else:
            return 'your speed is greater than the maximum!!!'

class SportCar(Car):
    def info_sportCar(self):
        print(f'this is Sport Car. Color {self.color}, name {self.name}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            return f'speed now -{self.speed}'
        else:
            return 'your speed is greater than the maximum!!!'

class PoliceCar(Car):
    def info_PoliceCar(self):
        if self.is_polise == True:
            print(f'This is police car. Color {self.color}, name {self.name}')

town_car1 = TownCar(70, 'red', 'mazda', False)
print(town_car1.show_speed())
print(town_car1.stop())

sport_car1 = SportCar(150, 'red', 'mokan', False)
print(sport_car1.turn('left'))
print(sport_car1.show_speed())

work_car1 = WorkCar(30,'yellow', 'kamaz', False)
print(work_car1.show_speed())

police_car1 = PoliceCar(90,'white', 'toyota', True)
police_car1.info_PoliceCar()


# 5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        info_5 = 'Запуск отрисовки'
        return info_5


class Pen(Stationary):
    def draw(self):
        info_6 = f'Запуск отрисовки чернилами'
        return info_6


class Pencil(Stationary):
    def draw(self):
        info_7 = f'Запуск отрисовки карандашами'
        return info_7


class Handle(Stationary):
    def draw(self):
        info_8 = f'Запуск отрисовки маркером'
        return info_8

pen1 = Pen('pen')
print(pen1.draw())
pencil1 = Pencil('pencil')
print(pencil1.draw())
handle1 = Handle('handle')
print(handle1.draw())
print(handle1.title)