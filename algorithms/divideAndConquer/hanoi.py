import time
import sys
#TODO: Make a real move, no just a print
#moves = list()

steps = 0

def move(a,b):
    #print(a,"➡️",b)
    #moves.append((a,b))
    # I hate to use globals but is the best way to simplify the code
    global steps 
    steps += 1
def hanoi(n,start,end):
    if n == 1: return move(start,end)
    other = 6 - (start + end)
    hanoi(n-1,start,other)
    move(start,end)
    hanoi(n-1,other,end)

size = int(sys.argv[1])
t0 = time.time()
hanoi(size,1,3)

#print(moves)
print("Steps ::",steps)
print("Time :: ",int((time.time()-t0)*1000))
print(2**size -1)