class Employee:
    company = "Apple"
    def show(self):
        print(f"the name of the employee is {self.name} and the company name is {self.company}")
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
employee = Employee()
employee.name = "Alok"
employee.show()
Employee.change_company("Google")
employee.show() 
print(Employee.company)