dictionary = {
    "harry" : "human being",
    "spoon" : "object"
}
print(dictionary["harry"])
print(dictionary.get("spoon")) # dont raise error
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for key in dictionary.keys() : 
    print(dictionary[key])
    
for key,value in dictionary.items() : 
    print(key ,"->", value)
    
first_dictionary = {
    "Math" : 75,
    "MIL" : 98,
    "Science" : 87
}
second_dictionary = {
    "history" : 98,
    "geography" : 97
}

print(first_dictionary.update(second_dictionary))
print(second_dictionary.clear())
print(first_dictionary)
print(second_dictionary)
first_dictionary.popitem()
print(first_dictionary)
del dictionary