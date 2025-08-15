
try : 
    number = int(input("Enter a number to get the table of it : "))
    print(f"The table of the number you entered is {number}")
    for i in range(1,11) : 
         print(f"{number} * {i} = {number * i}")
         
except Exception as error : 
    print("To get the multiplication table you cant give a string",error)
    
print("some important line of code")

try :
    number = int(input("Enter a specific number to get a value between 0 and 2"))
    number_list = [2,3,4]
    print(number_list[number])
except IndexError : 
    print("Entered the number is not in index")
    
def using_finally() : 
    try : 
        number = int(input("Enter a number to get the name : "))
        name_list = ["Alok","pradeep","Debasish"]
        return name_list[number]
    except Exception as error : 
        return error
    finally : 
        print("completed")
        
output = using_finally()
print(output)