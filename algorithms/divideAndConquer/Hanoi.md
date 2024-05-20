# Hanoi towers

## The code explained

The function move is the one that performs the one by one moves.
`````hanoi(n,start,end)``````

### The move(a,b) function (TL:DR)

Depending on the date you're reading this you could find a simple console output with the start and end numbers (ej: 1 3) or a more funier version with emoticons (ej: 1➡️3) or a list of movements with the iterations count. If you are from a more far future may be you'll find a beautiful animation that shows how every single piece of the towers move gracefully towards its destination, may be is an interactive animation where you can play with the towers trying to solve them by yourselve. May be that animation works on your VR in a perfect 3d simulation, or 4xd then you can feel the texture of the wood (may be already extinted) and hear the sound of the pieces falling and hitting between them. If you're on the last case, I feel sorry for you and deeply apollogize for fuck the planet up, I hope you live in a happy place in mars

## The hanoi(n,a,b) function

This is where Recursion starts, the idea is to create a recursive function to move the hanoi tower.

## Parameters

### n

The *n* parameter is the depth or the length of the tower. Also represents the n^th element, the one at the bottom

### start and end

The *start* parameter is the pilar where the tower is before move and the *end* parameter is the pilar destination for the tower
`````hanoi(n,start,end)``````

## The function's body

If the tower is a single unit, then we just move it. Assuming that all the pilars are empty OR has a biger item on top.

````` python
if n == 1: return move(start,end)
`````

The first time I realize the way to find the *other* pilar was a Wow moment. Think about it, if you have 3 pilars,one,two and three, you can't have the same pilar as start and end, so you always has 2 pilars selected to be start or end. So the max posible sum of the value of that pilars is where 2 and 3 are selected as start and end, without a particular order
**2+3=5**

In this case, the *other* pilar should be **one**

Other case is the min sum of the selected pilars which is **1+2=3**
In this case *other* should be **three**

And the option left. **1+3=4**. *Other* should be **two**

So the relationship with other and the sums of start and end are (3:3), (2:4) or (1:5). Notice that **all of them sums 6**
So **6 - (start + end)** should give us the *other*'s position

````` python
other = 6 - (start + end)
`````

### Recursion

We call the same function, moving the rest of the tower to an*other* place first

````` python
hanoi(n-1,start,other)
`````

Once we move the top of the tower, We can now move the base to its final destiny

````` python
move(start,end)
`````

Now that We have the bottom base on the final place, We move the tower We move in the first place on top of it

````` python
hanoi(n-1,other,end)
`````

And that's it... Really, that's it

## Try it

The basic one, a tower of 3 from the pilar one to the pilar 3

````` python
hanoi(3,1,3)
`````

A little less easy

````` python
hanoi(5,1,3)
`````

A hard one

````` python
hanoi(10,1,3)
`````

And a slow one

````` python
hanoi(50,1,3)
`````

### Benchmarking

At the end of the code you´ll find some code to benchmarking. I basically messure the iterations that each execution makes

````` python
print("Steps ::",steps)
`````