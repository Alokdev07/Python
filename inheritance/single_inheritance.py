class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name,species="dog")
        self.breed = breed
    def make_sound(self):
        print("bark")
        
dog = Dog("dog","doggerman")
dog.make_sound()
animal = Animal("dog","doggerman")
animal.make_sound()