#!/usr/bin/python3

# This is the graphA.png representation in his dictionary form
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(G,v):
  if v not in visited:
    print(v,end=" ")
    visited.add(v)
    for neighbour in G[v]:
        dfs(G,neighbour)

dfs(graph,'A')