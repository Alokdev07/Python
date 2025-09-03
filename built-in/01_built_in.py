list = [1,2,3,4]
print(dir(list)) # dir method use to see all the methods of this classes

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
person = Person("Alok",12)
print(person.__dict__) # convert all the items as dictionary in the class

print(help(person))