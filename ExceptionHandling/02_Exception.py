number = int(input("Enter a number between 5 to 9"))
if(number < 5 or number > 9) :
    raise ValueError("Enter number not between 5 to 9")