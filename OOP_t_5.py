"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery :

    def __init__(self, title):
        self.title = title
                
    def draw(self):
        print("Start draw",end="")
        
#Pen , Pencil , Handle 



class Pen(Stationery):

    def draw(self):
        super().draw()
        print(" by Pen ")

class Pencil(Stationery):

    def draw(self):
        super().draw()
        print(" by Pencil ")
       
class Handle(Stationery):

    def draw(self):
       print("Start draw by Handle ")
       
s1 = Pen("my_Pen")
s2 = Pencil("my_Pencil")
s3 = Handle("my_Handle")
s1.draw()
s2.draw()
s3.draw()
