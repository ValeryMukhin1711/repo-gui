#Задача 5
l = [i for i in range (10, 101) if i%2 ==0]
print (l)
#m = reduce (lambda a, x: a + x, l)

counter = 0
m = 1
while counter < len(l):
    m = m*l[counter]
    counter += 1
print (m)
