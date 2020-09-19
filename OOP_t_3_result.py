class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]

    def get_fullname(self):
        return f"{self.name} {self.surname}"    



p1 = Position("Bill","White","agent",{"wage" : 3000, "bonus" : 500})
p2 = Position("Homer","Smith","clerk",{"wage"  : 9000, "bonus" : 700})
p3 = Position("Sam","Green", position = "driver", income ={"wage"  : 5000, "bonus" : 300})
my_list =[p1,p2,p3]
for i in my_list:
    print(f" FullName: {i.get_fullname()}\t income {i.get_total_income()}")
