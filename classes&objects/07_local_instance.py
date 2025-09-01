class Employee:
    company_name = "Apple"
    def __init__(self,name):
        self.name = name
        self.raise_amount = 1.2
        
    def show_details(self):
        print(f"the employee name is {self.name} and the raise amount is {self.raise_amount} and works in {Employee.company_name}")
        
employee = Employee("Alok")
employee.raise_amount = 1.3
employee.show_details()
Employee.company_name = "Apple india"
Employee.show_details(employee)