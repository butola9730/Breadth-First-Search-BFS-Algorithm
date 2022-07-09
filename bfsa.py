
 
 def bfs(adjacencyList, vertex):
    visitedSet = set()
    queue = []
    visitedSet.add(vertex)
    queue.append(vertex)
    
    result = []
    while queue:
        v = queue[0]
        result.append(v)
        queue = queue[1:]
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                visitedSet.add(neighbor)
                queue.append(neighbor)
    return result

print(bfs(adjacencyList, 'A'))
