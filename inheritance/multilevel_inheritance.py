class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"The name of the animal is {self.name} and species {self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species = "dog")
        self.breed = breed
    def show_details(self):
        print(f"The breed of the animal is {self.breed}")    
class Golden_retriver(Dog):
    def __init__(self,name,color):
        super().__init__(name,breed = "golden retriver")
        self.color = color
    def show_details(self):
        print(f"The name of the animal is {self.name} and the color of the animal is {self.color} and the breed of the animal is {self.breed} and the species of the animal is {self.species}")   
    
golden_retriver = Golden_retriver("Alpha","Black")
golden_retriver.show_details()