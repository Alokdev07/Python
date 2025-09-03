class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i , self.j+x.j,self.k + x.k)
    
first_vector = Vector(2,3,4)
second_vector = Vector(3,4,5)
print(first_vector+second_vector)
print(type(first_vector+second_vector))