#!/usr/bin/python3
# this file starts with a copy of Helps/ficonacci.py
import sys
import time
class Solution:
    # A counter just for time meassuring
    count=0
    # Dictionary to store previus computed subproblems
    # We fill it with 0 and 1 because they're the monst common problems to solve (That's Dynamic Programming)
    # Without 0 and 1 in the Dict, this is only memorization, not Dynamic programming
    memory=dict({0:0,1:1,2:1})
    def fibonacci(self,n:int):
        # self.count is just for time meassuring, is not part of the algoritm as sell as n parameter
        self.count+=1
        if n < 0: # This is for errors control in case that n is not a uint
            raise ValueError("invalid index!")
        if n == 0: 
            return 0 
        if n == 1: 
            return 1 
        # Here we use memorization here, first we check if the computed n is not in the Dictionary already
        if(self.memory.get(n) == None):
            result=self.fibonacci(n - 1) + self.fibonacci(n - 2)
            # Once we compute the result of the n subproblem we store it the dictionary
            self.memory[n]=result
            # And return the result
            return result
        else:
            return self.memory.get(n)

# Call it from your console!!
#$ python fibonacciWithMemorization.py 20
t0= time.time()
sol = Solution()
fb = [sol.fibonacci(i) for i in range(int(sys.argv[1]))]
print(str(fb))
t1 = time.time() - t0
print("Time elapsed: ", t1)
print("Iterations",sol.count)
"""
# Calling both algorithms and meassuring their time and iterations. 
# Commonly the basic one will be the fastest whe u use les than 10 as parameter 
# But check the Iterations count (Amazing!)

❯ python fibonacciWithMemorization.py 30 && python Helps/fibonacci.py 30
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
Time elapsed:  0.00013780593872070312
Iterations 86
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
Time elapsed:  1.5958778858184814
Iterations 4356586
"""
