#!/usr/bin/python3
from thegraph import graph

visited = set() # Set to keep track of visited nodes.

def dfs(G,v):
  if v not in visited:
    print(v,end=" ")
    visited.add(v)
    for neighbour in G[v]:
        dfs(G,neighbour)

dfs(graph,'A')
print(visited)