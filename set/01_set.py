first_set = {2,3,4,5,4,3,}
print(first_set)
empty_set = {} # this type of empty set is dictionary
print(type(empty_set))
original_empty_set =  set()
print(type(original_empty_set))

for elem in first_set : 
    print(elem)
    
first_number_set = {1,2,3,4}
second_number_set = {5,6,7,8}
print(first_number_set.union(second_number_set))
print(first_number_set.intersection(second_number_set))
first_number_set.update(second_number_set)
print(first_number_set)
first_number_set.intersection_update(second_number_set) # First number = second number with intersection function
print(first_number_set)

Another_first_number = {1,2,3,4,5}
Another_second_number = {3,4,5,6,7}
print(Another_first_number.symmetric_difference(Another_second_number))
print(Another_first_number.difference(Another_second_number))
print(Another_first_number.isdisjoint(Another_second_number))
print(Another_first_number.issubset(Another_second_number))
print(Another_first_number.issuperset(Another_second_number))
Another_first_number.add(9)
print(Another_first_number)
Another_first_number.remove(9) # if not present error raise
Another_first_number.discard(9) # if not present error dont raise
removed_number = Another_first_number.pop() # random value remove
print(removed_number)

del first_set # to delete the entire set
second_number_set.clear() # to clear the set

if 4 in Another_first_number : 
    print(True)
