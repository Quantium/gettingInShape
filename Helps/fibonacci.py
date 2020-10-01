#!/usr/bin/python3
import sys
import time
class Solution:
    count=0
    def fibonacci(self,n):
        self.count+=1
        if n < 0:
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
"""
Ej, when calling fibonacci(4) the funcion is called 9 times, so it is an algorithm of O(2N)
->fibonacci(4)              1
    ->fibonacci(3)          2
        ->fibonacci(2)      3
            ->fibonacci(1)  4
            ->fibonacci(0)  5
        ->fibonacci(1)      5
    ->fibonacci(2)          7
        ->fibonacci(1)      8
        ->fibonacci(0)      9
"""