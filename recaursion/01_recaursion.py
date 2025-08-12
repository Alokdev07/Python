# factorial of 5 = 5*4*3*2*1
             # 4 = 4*3*2*1
             # 3 = 3*2*1
             
def factorial_of_number(n) : 
    if(n == 0 or n ==1) :
        return 1
    else :
        return n * factorial_of_number(n-1)
fact_number = factorial_of_number(5)
print(fact_number)