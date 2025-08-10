x = int(input("enter the value of x : "))
match x :
    case 0 :
        print("entered values is 0")
    case 1 : 
        print("entered the value of x is 1")
    case _ if(x == 5) : 
        print("the value is greater than 5")
    case _ : 
        print("entered the value of x > 10")