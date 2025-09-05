import datetime
import time

def using_while():
    i = 0
    while i < 500000:
        print(i)
        i += 1

def using_for():
    for i in range(5000000):
        print(i)

# Record start time
start_time = time.time()

using_while()
using_for()

# Record end time
end_time = time.time()

# Calculate duration
duration = end_time - start_time

print(f"Time taken to run this program is {duration:.6f} seconds")
