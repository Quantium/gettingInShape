#!/usr/bin/python3

# This is the graphA.png representation in his dictionary form
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'], # this is irrelevant for trees
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue (FIFO)

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) # geting out the _first_ element
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')