#super keyword
class Parent():
    def parent_method(self):
        print("This is in the parent class")
class Child(Parent):
    def child_method(self):
        print("This is in the child class")
        super().parent_method()
child_object = Child()
child_object.child_method()
