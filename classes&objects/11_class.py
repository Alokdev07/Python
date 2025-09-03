class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius**2
    
rectangle = Shape(3,4)
print(rectangle.area())
circle = Circle(5)
print(circle.area())