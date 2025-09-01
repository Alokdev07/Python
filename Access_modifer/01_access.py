class Student:
    def __init__(self):
        self.__name = "Alok bhuyan" # to create private method or variable use __
        self.__age = 12
        
new_student = Student()
print(new_student._Student__name)
print(new_student._Student__age)

class Teacher:
    def __init__(self):
        self._name = "Alok bhuyan"
        self._age = 52
        
new_teacher = Teacher()
print(new_teacher._name)
print(new_teacher._age)