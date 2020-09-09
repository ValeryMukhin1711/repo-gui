#Задача 4

lis = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lis2 = [lis[i] for i in range (len(lis)) if lis.count(lis[i]) < 2]
print (lis2)
