class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name of the employee is {self.name}")
        
class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The name of the dance is {self.dance}")
        
class Dancer_Employee(Dancer,Employee):
    def __init__(self, dance,name):
        super().__init__(dance)
        Employee.__init__(self,name)
        
dancer_employee = Dancer_Employee("Kathak","Alok")
print(dancer_employee.name,dancer_employee.dance)
dancer_employee.show()