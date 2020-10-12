#!/usr/bin/python3
# this file starts with a copy of Helps/ficonacci.py
import sys
import time
class Solution:
    # A counter just for time meassuring
    count=0
    def fibonacci(self,n:int):
        # self.count is just for time meassuring, is not part of the algoritm as sell as n parameter
        self.count+=1
        if n < 0: # This is for errors control in case that n is not a uint
            raise ValueError("invalid index!")
        if n == 0: 
            return 0 
        if n == 1: 
            return 1 
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

# Call it from your console!!
#$ python fibonacci.py 9
t0= time.time()
sol = Solution()
fb = [sol.fibonacci(i) for i in range(int(sys.argv[1]))]
print(str(fb))
t1 = time.time() - t0
print("Time elapsed: ", t1)
print("Iterations",sol.count)