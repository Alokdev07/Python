# First basic project: Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = int(input("What should I do with these numbers?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter a number (1-4): "))

if operation == 1:
    print("Result:", num1 + num2)
elif operation == 2:
    print("Result:", num1 - num2)
elif operation == 3:
    print("Result:", num1 * num2)
elif operation == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation number. Please enter 1, 2, 3, or 4.")
