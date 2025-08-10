def calculateGmean(a,b) : 
    mean = (a*b)/(a+b)
    print(mean)
    
    
# Gmean1 = calculateGmean(3,4)



def calculate_Gmean_According_To_greater_value(a,b) :
    if(a > b) : 
        calculateGmean(a,b)
    else :
        print("enter first number greater")
        
calculate_Gmean_According_To_greater_value(8,2)

def calculate_sum(a,b) : 
    pass