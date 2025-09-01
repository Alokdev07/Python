with open("png.txt","r") as file : 
   lines =  file.readlines()
new_line = []
for index,line in enumerate(lines,start=1):
    line = line.strip()
    if "." in line : 
        name,extension = line.rsplit(".",1)
        new_line.append(f"{index}.{extension}\n")
    else:
        new_line.append(f"{index}")
with open("png.txt","w") as file : 
    file.writelines(new_line)