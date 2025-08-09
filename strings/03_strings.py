# strings are immutable
name = "Harry"

print(name.upper())

print(name.lower())

name_with_exCh = "Alok!!!!"

print(name_with_exCh.rstrip("!"))

print(name.replace("Harry","Alok")) # Change all occurrence

Fullname = "alok bhuyan"

print(Fullname.split(" "))

print(Fullname.capitalize())

print(Fullname.center(50))

print(Fullname.count("a"))

print(Fullname.endswith("!"))

str1 = "welcome to the console"

print(str1.endswith("to",4,10))

print(Fullname.find("a"))

print(Fullname.isalnum()) # contains letters numbers - true

print(Fullname.isalpha()) #contains only letters - true

print(Fullname.islower())

print(Fullname.isprintable())   

print(Fullname.isspace())

print(Fullname.istitle())

print(Fullname.startswith("a"))

print(Fullname.swapcase())

print(Fullname.title())