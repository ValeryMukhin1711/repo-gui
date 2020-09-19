
class Cell:
    def __init__(self, count):
        self.count = count


    def __add__(self, other):
        return Cell(self.count + other.count)
    
    def __str__(self):
            return f"object Cell with  ({self.count}) yacheek "


    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return Cell(self.count - other.count)
        else:
            f"Imposible substrate "
            
            
    def __mul__(self, other):
        return Cell(self.count * other.count)            

    def __truediv__(self, other):
        return Cell(int(self.count / other.count))

    def make_order(self,number):
        k = 0
        i = 0
        next_row = True
        st = ""
        while next_row:
            if k != 0:
                st = st +"\n"
            while i < number:
                st = st+"*"
                i +=1
                k +=1
                if k > self.count - 1 :
                   next_row = False
                   break
    

            print(f"st\n{st} \ni= {i} k= {k}")
            i = 0            
#            j = input("press enter")
        return st    
            



c_1 = Cell(10)
c_2 = Cell(30)
print((c_1 + c_2))
print(c_1 - c_2)
print(c_2 - c_1)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_2 / c_1)
print(c_2.make_order(4))
