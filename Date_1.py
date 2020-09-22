"""
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В
рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с
декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
"""

class Date :
    @classmethod
    def to_int(cls,inp_date,part):
        m_list = (inp_date).split("-")
        
        if part == "d":
            return int(m_list[0])
        elif part == "m":
            return int(m_list[1])
        elif part == "y":
            return int(m_list[2])
        
    
    @staticmethod
    def str_validate(data_string):
        r = True
        m_list = data_string.split("-")
        if int(m_list[0]) < 0 or int(m_list[0]) > 31:
            r = False
        elif int(m_list[1]) < 0 or int(m_list[1]) > 12:
            r = False
        elif int(m_list[1]) < 0 or int(m_list[1]) > 2020:
            r = False
        return r
    
    def __init__ (self,date):
        self.date = date

    def date_to_int(self,part):
        m_list = (self.date).split("-")
        
        if part == "d":
            return int(m_list[0])
        elif part == "m":
            return int(m_list[1])
        elif part == "y":
            return int(m_list[2])


        
    def date_validate (self):
        r = True
        m_list = (self.date).split("-")
        if int(m_list[0]) < 0 or int(m_list[0]) > 31:
            r = False
        elif int(m_list[1]) < 0 or int(m_list[1]) > 12:
            r = False
        elif int(m_list[1]) < 0 or int(m_list[1]) > 2020:
            r = False
        return r

    
 
    
d = Date("10-12-2000")
d1 = Date("40-12-2000")
d2 = Date("04-14-2000")


for i in [d,d1,d2]:
    print(i.date)
    print(i.date_to_int("d"))
    print(i.date_to_int("m"))
    print(i.date_to_int("y"))
    print(f"validate date {i.date} ",end ="")
    print(i.date_validate())

#### Test @staticmethod  validate()  
print('\n#### Test @staticmethod  validate()')
test_list =["10-12-2000","40-12-2000","04-14-2000"]
for i in test_list:
    print(f" i {i}")
    print(f"Date.str_validate (\"{i}\") ",end ="")   
    print(Date.str_validate (i))  

#### Test @classmethod  to_int()
print('\n#### Test @classmethod  to_int()')    
for i in [d,d1,d2]:
    print(i.date)
    print("day " + str(Date.to_int(i.date,"d")))
    print("month " + str(Date.to_int(i.date,"m")))
    print("year " + str(Date.to_int(i.date,"y")))



