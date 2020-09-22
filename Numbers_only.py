"""
3. Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу
исключения на реальном примере. Необходимо запрашивать у пользователя
данные и заполнять список. Класс-исключение должен контролировать
типы данных элементов списка.
"""

class Type_isnt_int(Exception):   
    def __init__ (self, text):
        self.text = text

def ch_inp(str):
    my_list =list(inp)
    out =""
    for i in my_list:
        if i in list("0123456789"):
            out +=i
        else:
            raise Type_isnt_int(f"Your string '{inp}' isn't number")
    return int(out)      

print("Start")            
inp = input('Input next number or "stop" for finish ')
if inp =="":
    inp =" "
out_list=[] 
while inp != "stop" :
    
    
    try:
        out_list.append(ch_inp(inp))
    except Type_isnt_int as ex:
        print(ex)
    while True:
        inp = input('Input next number or "stop" for finish ')
        if inp == "":
            pass
        else:
            break
    
print(f"result list {out_list}")    

print("Buy")

   
    
    

