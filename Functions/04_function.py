from functools import reduce

def cube(x):
    return x**3
def filter_function(x):
    return x%2 == 0

number_list = [1,2,3,4,5,6]

new_number_list = list(map(cube,number_list))
filter_number_list = list(filter(filter_function,number_list))
print(new_number_list)
print(filter_number_list)

sum_of_numbers = reduce(lambda x,y : x+y,number_list)
print(sum_of_numbers)