numbers = [1,2,3,4,6]
while(n := len(numbers)) > 0:
    print(numbers.pop())
    
foods = list()
while(food := input("Enter the fruits name you liked ? ")) != "quit":
    foods.append(food)
    
print(foods)