class Shapes:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def displayArea():
        pass
class Triangle(Shapes):
    def __init__(self, length, height):
        super().__init__(length,height)
        self.height = height
        
    def calculate(self):
        area = (self.length * self.height)/2
        return area

class Circle(Shapes):
    def __init__(self, width,pi):
        super().__init__(width,pi)
        self.pi = pi
        
    def calculatecirc(self):
        radius = self.width / 2
        area = self.pi * radius ** 2
        return area

shape = Triangle(12,56)
print("The area is:", shape.calculate())
shape2 = Circle(13,3.1415962)
print("The area is:", shape2.calculatecirc())
