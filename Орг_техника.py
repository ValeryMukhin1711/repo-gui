"""4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
сканер, ксерокс). В базовом классе определить параметры, общие
для приведенных типов. В классах-наследниках реализовать параметры, уникальные
для каждого типа оргтехники.
"""
class Warehouse:
#    printers_list = []
#    scaners_list = []    
#    xeroxs_list = []
    total_list = []
    warehouse_list =[]

    def put_to_warehouse(self):
        Warehouse.warehouse_list.append(self)
        self.location = "warehouse"

            
    def get_from_warehouse(self,location):
        self.location = location
        Warehouse.warehouse_list.remove(self)
        print(f"{self.type_eq} number({self.number}) moved to {self.location}")

    
class Office_equipment(Warehouse):
    def __init__(self, number, type_eq, model, location):
        self.number = int(number)
        self.type_eq = type_eq
        self.model = model
        self.location = location
        Warehouse.total_list.append(self)


class Printers(Office_equipment):
    def __init__(self, number, type_eq, model, location, page_min):
        super().__init__(number, type_eq, model, location)
        self.page_min = page_min

        
class Scaners(Office_equipment):
    def __init__(self, number, type_eq, model, location, dpi):
        super().__init__(number, type_eq, model, location)
        self.dpi = dpi


class Xeroxs(Office_equipment):
    def __init__(self, number, type_eq, model, location, page_min):
        super().__init__(number, type_eq, model, location)
        self.page_min = page_min

p1 = Printers(1,"Printer","HP","room1",20)
p2 = Printers(14,"Printer","HP_1","room4",20)
print(p1.type_eq)
s1 = Scaners(2,"Scaner","Epson","room2",600)
print(s1.type_eq)
x1 = Xeroxs(3,"Xerox","MB","room3",60)
print(x1.type_eq)
t_list = [p1,s1,x1,p2]
for i in t_list:
    print(i.type_eq)
    i.put_to_warehouse()
    for j in i.total_list:
        print(f"{j.model} {j.location}, ",end ="")
print()        
p1.get_from_warehouse("room1")
for j in p1.total_list:
        print(f"{j.model} {j.location}, ",end ="")
        
####Validation

def action():
    inp = input("\nAction: \n1 - new \n2 - to_warehouse \n3 - from_warehouse\
\n4 - List warehouse \n5 - List total \n? ")
    if inp =="1":
        pass
    elif inp =="2":

        for i in Warehouse.total_list :
            print(f" {i.number} {i.type_eq} {i.model}")
        while True:
            inp = input("Choose device from list, enter device number ")
            try:
                inp = int(inp)
                break
            except:
                print("Device number must be digital!")
                
        for i in Warehouse.total_list :
            print(f"inp {inp}")
            if i.number  == int(inp):
                print(f"i.number {i.number} {i.model}")
                i.put_to_warehouse()
        
    elif inp =="3":
        
        for i in Warehouse.total_list :
            print(f" {i.number} {i.type_eq} {i.model}")
        inp = input("Choose device from list, enter device number ")
        i_room = input("Input new location ")
        for i in Warehouse.total_list :
            if i.number  == int(inp):
                    i.get_from_warehouse(i_room)
        pass
    elif inp =="4":
        print("\nWarehouse:-")        
        for i in Warehouse.warehouse_list :
            print(f"{i.number} {i.type_eq} {i.model} {i.location}")
    elif inp =="5":
        print("\nTotal:-")        
        for i in Warehouse.total_list :
            print(f"{i.number} {i.type_eq} {i.model} {i.location}")        
    else:
        print("No input - no action")
        return "buy"
    
while True:
    if action() == "buy":
        break
