#create a generator

def my_generator():
    for i in range(5):
        yield i
generator = my_generator()
print(next(generator))
print(next(generator))
print(next(generator))