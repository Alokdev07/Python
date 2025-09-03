class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod 
    def from_string(cls,data):
        name,age = data.split("-")
        return cls(name,age)
    def show(self):
        print(f"The employee name is {self.name} and his salary is {self.salary}")
        
employee = Employee.from_string("Alok-20000")
employee.show()
