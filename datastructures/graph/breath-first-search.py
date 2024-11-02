#!/usr/bin/python3
from thegraph import graph

visited = set() # List to keep track of visited nodes.
queue = []   #Initialize a queue (FIFO)

def bfs(G, v):
  visited.add(v)
  queue.append(v)

  while queue:
    s = queue.pop(0) # geting out the _first_ element
    print (s, end = " ") 
    
    for neighbour in G[s]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

bfs( graph, 'A')
print(visited)