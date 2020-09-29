#!/usr/bin/python3
import sys
import time
def fibonacci(n):
    if n < 0:
        raise ValueError("invalid index!")
    if n == 0: 
        return 0 
    if n == 1: 
        return 1 
    return fibonacci(n - 1) + fibonacci(n - 2)

# Call it from your console!!
#$ python fibonacci.py 9
t0= time.clock()
fb = [fibonacci(i) for i in range(int(sys.argv[1]))]
print(str(fb))
t1 = time.clock() - t0
print("Time elapsed: ", t1)