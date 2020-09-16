"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import time
print("Start")
class TrafficLight():
    __color = ""
    __count = 0

    
    def running (self,color):
        __color = color
        print("Start from <<<<" + __color + ">>>> color")
        if __color =="Red":
           
            print("TrafficLight color is Red")
            TrafficLight.__count_down(7)
            print("TrafficLight color is Yellow")
            TrafficLight.__count_down(2)
            print("TrafficLight color is Green")
            TrafficLight.__count_down(4)
        if __color =="Yellow":
          

            print("TrafficLight color is Yellow")
            TrafficLight.__count_down(2)
            print("TrafficLight color is Green")
            TrafficLight.__count_down(4)
        if __color =="Green":

            print("TrafficLight color is Green")
            TrafficLight.__count_down(4)

 
    def __count_down(c):
        
        i = 0
        while i < c+1:
            print(str(i) + " ",end="")
            time.sleep(1)
            i +=1
        print()

            
t_l = TrafficLight()
t_l.running("Red")
t_l.running("Yellow")
t_l.running("Green")
print("Stop")
