tup = (1,3,4)
print(type(tup))

# when a single value is in parenthesis it is not considered as tuple

tuple1 = ("harry",1,True)
print(tuple1)

if 4 in tup : 
    print("yes")
    
print(tuple1[1:3])

new_tuple = ("Alok","Akash","Rajaram","Pati")
List_tuple = list(new_tuple)
List_tuple.append("Kanha")
Another_tuple = tuple(List_tuple)
print(Another_tuple)

count_tuple = Another_tuple.count("Alok")
print(count_tuple)

occurrence_tuple = Another_tuple.index("Alok",0,3)
print(occurrence_tuple)