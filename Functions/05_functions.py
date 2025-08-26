def greet(function) : 
    def modified_function(*args,**kwargs):
        print("Good Morning")
        function(*args,**kwargs)
        print("Thanks for using this function")
    return modified_function
@greet     
def add_function(first_number,second_number):
    print(first_number+second_number)
    
add_function(4,5)