class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def show_details(self):
        print(f"The name of the employee is {self.name} and id is {self.id}")
        
class Programmer(Employee):
    def __init__(self, name, id,language):
        self.language = language
        super().__init__(name, id)
        
    def show_details(self):
        print(f"The name of the employee is {self.name} and id is {self.id} and language is {self.language}")

new_employee = Employee("Alok Bhuyan",101)
new_employee.show_details()
another_employee = Programmer("Alok bhuyan",102,"python")
another_employee.show_details()