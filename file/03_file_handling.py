with open("new_file.txt",'r') as f: 
    print(type(f))
    # Move to the 10 th byte of the file
    f.seek(10)
    print(f.tell())
    # Read the next 5 bytes
    data = f.read(5)
    print(data)
    
with open("sample.txt",'w') as sample : 
    sample.write("Hello world !")
    sample.truncate(5)
    
with open("sample.txt",'r') as sample : 
    print(sample.read())