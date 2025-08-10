import time
now = time.localtime()
current_time = time.strftime("%H%M", now)
current_format = time.strftime("%p",now)
print(current_format,current_time)
if(int(current_time) > 06.00 and current_format == "AM") : 
    print("good morning")
elif(int(current_time) > 12.00 and current_format == "PM") : 
    print("good afternoon")
else :
    print("good evening")