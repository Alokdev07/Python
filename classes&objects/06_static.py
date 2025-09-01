class Math:
    def __init__(self,num):
        self.num = num
        
    def add_to_num(self,num):
        print(self.num + num)
        
    @staticmethod
    def static_add(first_number,second_number):
        print(first_number+second_number)
        
math = Math(5)
math.add_to_num(9)
Math.static_add(2,3)