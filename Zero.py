class DevZero(ZeroDivisionError):   
    def __init__ (self, text):
        self.text = text

def division(a,b):
    try:
        if b == 0:
            raise DevZero("You try divide by zero")
    except DevZero as dz:
        print(dz)
    else:
        return a/b
        
print(division(4,2))
print(division(6,0))
    
