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

visited = [] # List to keep track of visited nodes.
stack = []     #Initialize a stack (LIFO)

def bfs(visited, graph, node):
  visited.append(node)
  stack.append(node)

  while stack:
    s = stack.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')