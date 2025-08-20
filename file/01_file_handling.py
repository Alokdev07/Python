file = open(r"C:\Users\HP\OneDrive\Desktop\python\virtual_environment.md","r")
print(file.read())
file.close()

new_file = open("new_file.txt",'w')
new_file.write("hello world")
new_file.close()

new_file = open("new_file.txt",'a')
new_file.write(" to alok")
new_file.close()

with open("new_file.txt",'a') as new_file : 
    new_file.write(" appreciate")