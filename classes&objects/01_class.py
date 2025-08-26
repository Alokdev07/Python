class Person : 
    name = "Alok"
    occupation = "Software developer"
    net_worth = 10
    def information(self):
        print(f"The name of the person is {self.name} and occupation is {self.occupation} and net_worth of the person is {self.net_worth}")
    
A = Person()
A.name = "Subham"
A.occupation = "Ai integrated Software developer"

A.information()