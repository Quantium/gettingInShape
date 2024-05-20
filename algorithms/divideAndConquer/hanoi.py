#TODO: Make a real move, no just a print
#moves = list()

steps = 0

def move(a,b):
    print(a,"➡️",b)
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


#hanoi(3,1,3)
hanoi(5,1,3)
#hanoi(10,1,3)
#hanoi(50,1,3)

#print(moves)
print("Steps ::",steps)