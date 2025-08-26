class Person : 
    def __init__(self):
        print("Hey i am a person")
first_person = Person()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"the name of the student is {self.name} and the age of the student is {self.age}")
        
first_student = Student("Alok",12)
first_student.info()