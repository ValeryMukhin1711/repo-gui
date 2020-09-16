class Road:

    def __init__(self, width, length):
        self.__width = width
        self._length = length

    def get_width(self):
        return self.__width


    def get_length(self):
        return self._length


    
    def get_mass_asphalt(self,thickness):
        return self.__width * self._length*25*thickness

r1 = Road(1000,3)
r2 = Road(20000,12)
 

print("r1.get_width() = ", r1.get_width())
print("r1.get_length() = ", r1.get_length())
print("r1.get_mass_asphalt(5) = ", r1.get_mass_asphalt(5))
 
print("-----------------")


print("r2.getWidth() = ", r2.get_width())
print("r2.get_length() = ", r2.get_length())
print("r2.get_mass_asphalt(10) = ", r2.get_mass_asphalt(10))

