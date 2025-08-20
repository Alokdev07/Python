import os

if( not os.path.exists("data")) : 
    os.mkdir("data")

for i in range(0,5) : 
    os.mkdir(f'data/day{i}')
    
for i in range(0,5) : 
    os.rename(f'data/day{i}',f'data/tutorial{i}')
    
folders = os.listdir("data")

for folder in folders : 
    print(folder)
    
os.system('cmd')
print(os.getcwd())