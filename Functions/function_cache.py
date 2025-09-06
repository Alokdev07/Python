import functools
import time

@functools.lru_cache(maxsize=None)
def complex_function(number):
    time.sleep(5)
    return number*5

print(complex_function(20))
print("done for 20")
print(complex_function(5))
print("done for five")
print(complex_function(20))
print(complex_function(5))