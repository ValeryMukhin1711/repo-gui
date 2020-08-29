#Задача_2

sec = int (input ('Пожалуйста, введите время в секундах '))
hours = sec // 3600
minutes =  (sec - (hours * 3600)) // 60
seconds = sec % 60
time = "{0} : {1} : {2}".format(hours, minutes, seconds)
print ("Это время составляет " + time)


