class Employee:
    def __init__(self):
        self.name = "Harry"
    def __len__(self):
        index = 0
        for character in self.name:
            index = index+1
        return index
    def __str__(self):
       return (f"the name of the employee is {self.name}")
    def __call__(self):
       print("hey i am good")
employee = Employee()
print(employee.name)
print(len(employee))
print(employee)
employee()