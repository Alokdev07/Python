def calculate_average(a = 9,b = 1) : # default value for function
    return print("the average of the 2 variable is ",(a+b)/2)
calculate_average(4,5)
calculate_average(b=5)
# keyword arg used to give data in any order
calculate_average(b=5,a=3)
# requirement arg are compulsory to give

# Arbitrary arguments

def calculate_average_arbitrary(*numbers) : # it take numbers of arg in single arg
    sum = 0
    print("type of numbers",type(numbers))
    for i in numbers : 
        sum = sum + i
    print("The average of given numbers is",sum/len(numbers))
    
calculate_average_arbitrary(3,4,5)

def name(**name) : # to take name as dictionary
    print("hello",name["fname"],name["lname"],name["mname"])
name(fname = "Alok",lname = "Bhuyan",mname = "Python")