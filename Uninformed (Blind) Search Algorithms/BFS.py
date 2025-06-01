from collections import deque

def bfs(graph, start, goal):
    
    visited  = set()
    queue = deque([[start]])

    while queue :
        print(queue) # for trace 
        path = deque.popleft(queue)
        node = path[-1]

        if node == goal :
            return path 
        
        if node not in visited :
            visited.add(node)
            sonsOfCurrentNode = graph[node]
            for son in sonsOfCurrentNode :
                new_path = list(path)
                new_path.append(son)
                queue.append(new_path)

    
    return []


# Example graph as adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

print(bfs(graph, 'A', 'G'))  # Output: ['A', 'D', 'G']