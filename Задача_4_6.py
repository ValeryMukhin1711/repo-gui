#Задача 6
#первый скрипт
from itertools import count
start = int(input("Введите начальное число "))
stop = int(input("Введите конечное число "))
for i in count(start):
    if i > stop:
        break
    else:
        print(i)
