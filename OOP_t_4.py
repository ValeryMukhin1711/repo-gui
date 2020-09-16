"""
4. Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов
методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print("Car " + self.name + " started")
        
    def stop(self):
        print("Car " + self.name + " stopped")
    
    def turn(self,direction):
        print("Car " + self.name + " turned to " + direction)
        
    def show_speed(self):
        print("Car " + self.name + " speed is " + str(self.speed))

#TownCar, SportCar, WorkCar, PoliceCar

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
#       print("Car " + self.name + " speed is " + str(self.speed))
        if self.speed > 60:
            print("Warning! Overspeed!")
class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Warning! Overspeed!")            

class SportCar(Car):
    pass
class PoliceCar(Car):
    pass
    

r1 = WorkCar(50,"red","Ford", False )
r2 = TownCar(100,"red","BMW", False) 
r3 = SportCar(200,"green","Lancha",False)
r4 = PoliceCar(250,"black","Dodge",True)
print("----------WorkCar----------")
r1.go()
r1.turn("right")
r1.show_speed()
print("----------TownCar----------")
r2.go()
r2.turn("up")
r2.show_speed()
print("----------SportCar---------")
r3.go()
r3.turn("left")
r3.show_speed()
print("----------PoliceCar--------")
r4.go()
r4.turn("left")
r4.show_speed() 
print("Stop")


