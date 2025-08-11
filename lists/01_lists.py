list = [1,2,3,4,5,6,7,8,9]

# print(list)

# print(type(list))

multi_type_list = ["Alok",12,True]

print(multi_type_list)

if 7 in list :
    print("yes")
else : 
    print("no")
    
if "arr" in "harry": # same things apply on string as well
    print("yes")
    
# print(list[1:-1:2])

lst = [i for i in range(4)]
print(lst)
lst = [i for i in range(10) if i%2 ==0]
print(lst)

New_list = [1,5,7,4,3]
New_list.append(2)
New_list.sort()
print(New_list)
New_list.reverse()
print(New_list)
print(New_list.index(2))
print(New_list.count(2))
copy_list = New_list.copy()
copy_list[0] = 1
print(copy_list)
copy_list.insert(0,7)
print(copy_list)
Another_list = [900,1000,1100]
copy_list.extend(Another_list)
print(copy_list)
