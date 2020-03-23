class Circle:
    def __init__(self,gradius):
        self.radius = gradius
    def calc_Area(self):
        return 2*3.14*self.radius**2
    def calc_Diameter(self):
        return self.radius**2

c1 = Circle(5)
print("Area of Circle : ",c1.calc_Area())
print("Diameter of Circle : ",c1.calc_Diameter())
