"""7. Реализовать проект «Операции с комплексными числами». Создайте
класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата."""

class ComplexNumber:
    def __init__ (self, r, i):
        self.r = r
        self.i = i
    def __str__ (self):
        return f"Complex number {self.r}+{self.i}i"
    
    def __add__ (self, other):
        r = self.r + other.r
        i = self.i + other.i
        return ComplexNumber (r, i)
    
    def __mul__ (self, other):
        r = self.r * other.r - self.i * other.i
        i = self.r * other.i + self.i * other.r
        return ComplexNumber (r, i)

n1 = ComplexNumber (1, 2)
n2 = ComplexNumber (3, 4)
n3 = n1 + n2
print (n3)
n4 = n1 * n2
print (n4)
