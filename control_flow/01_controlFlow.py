age = int(input("Enter your age : "))
print(age)
'''conditional operator
> - greater than
< - less than
== - equal to 
!= - not equal to 
>= - greater than equal to
<= - less than equal to 

'''
if(age > 18) : 
    print("you can drive")
else : 
    print("you can't drive")
    
apple_price = 20
budget = 200
if(budget - apple_price > 50) : 
    print("You can buy apple")
elif(budget - apple_price > 70) : 
    print("its okay can buy")
else :
    print("i cant buy an apple")
    
num = 10

if(num < 0) : 
    print("num is negative")
elif(num > 0) : 
    if(num <= 10) : 
        print("num is between 1 - 10")
    else : 
        print("Num is greater than 10")
else : 
    print("num is 0")