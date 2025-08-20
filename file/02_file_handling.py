file = open("new_file.txt",'r')
index = 0
while True : 
    index = index+1
    line = file.readline()
    if not line :
        print(line,type(line))
        break
    Math_mark = line.split(",")[0]
    science_mark = line.split(",")[1]
    sst_mark = line.split(",")[2]
    
    print(f"the marks appeared {index} student in math is {Math_mark}")
    print(f"the marks appeared {index} student in science {science_mark}")
    print(f"the marks appeared {index} student in sst is {sst_mark}")
   
   
write_lines = ["first_line \n","second_line \n","third_line \n"]
write_file = open("new_file.txt",'w')
write_file.writelines(write_lines)
write_file.close()