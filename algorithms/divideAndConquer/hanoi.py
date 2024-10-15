import time
import sys
#TODO: Make a real move, no just a print
moves = list()

steps = 0

def move(a,b):
    print(a,"➡️",b)
    moves.append((a,b))
    # I hate to use globals but is the best way to simplify the code
    global steps 
    steps += 1

def hanoi(n,start,target):
    if n == 1: return move(start,target)

    # Since the sum of the numbers of all three pegs is always 1 + 2 + 3 = 6, 
    # if we know two of the pegs (start and target), we can find the third one using:
    # \text{other} = 6 - (\text{start} + \text{target})
    other = 6 - (start + target)

    hanoi(n-1,start,other) # Hey, guy(s) above me, move from top of me (start) to the peg (other) that is not my target
    move(start,target) # Then I will move to my target
    hanoi(n-1,other,target) # Finally, you move from the peg you are in (other) back on top of me (target)

size = int(sys.argv[1])
t0 = time.time()
hanoi(size,1,3)

print(moves)
print("Steps ::",steps)
print("Time :: ",int((time.time()-t0)*1000))
print(2**size -1)