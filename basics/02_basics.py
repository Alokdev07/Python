# variable and data_type
a = 1
print(a)
b = "Harry"
print(b)
c = True
d = None
print("The type of a is : ",type(a))
print("The type of b is : ",type(b))
print("The type of c is : ",type(c))
print("The type of d is : ",type(d))

list1 = [1,1.2,[1,2],["Banana","Apple"],True] #mutable
print(list1)

tuple1 = (("Orange"),"Banana,Apple") #immutable
print(tuple1)

disc1 = {
    "name" : "alok",
    "age" : 29
    }
print(disc1)

#implicit typecasting

num1 = 1.9
num2 = 8
print(type(num1+num2))