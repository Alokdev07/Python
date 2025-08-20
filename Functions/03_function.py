def double(x):
    return x*2

double_lambda = lambda x : x*2
cube_lambda = lambda x : x**3
avg_lambda = lambda x,y : (x+y)/2

print(double_lambda(5))
print(cube_lambda(5))
print(avg_lambda(5,3))

def sum(function,first_value) :
    return 10 + function(first_value)

print(sum(double_lambda,4))