global_variable = 4
print(f"the global variable is {global_variable}")

def understand_local_variable() : 
    global_variable = 5 # it is the local variable in the function
    print(global_variable)
understand_local_variable()

def change_global_variable():
    global global_variable 
    global_variable = 6
    print(global_variable)

change_global_variable()
print(global_variable)
# we dont access local variable outside function