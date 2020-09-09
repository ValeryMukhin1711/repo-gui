#Задача 7

def fact ():
    n = 1
    n2 = int(input ("Введите натуральное число "))
    if n2 == 1:
        print ('факториал 1 равен 1')
    else:
        while n < n2:
            res = n * (n+1)
            n +=1
            print (f'факториал {n2} равен {res}')
    
fact ()
    
