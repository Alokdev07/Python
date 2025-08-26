class My_class : 
    value = 0
    def show(self):
        print(f"the value of the function is {self._value}")
    @property
    def double_value(self):
        return self._value**2
    @double_value.setter
    def double_value(self,new_value):
        self._value = new_value**2
        
new_class = My_class()
new_class.double_value = 3
new_class.show()