

def dfs_optimized(graph, start, goal):
    
    visited  = set()
    stack = [start] # store nodes instead of path
    parent = {start : None}

    while stack :
        node = stack.pop()

        if node == goal : # if noe is the goal draw the path 
            path = []
            while node is not None :
                path.append(node)
                node = parent[node]
            
            return path[::-1] # reverce the list 
        
        if node not in visited :
            visited.add(node)
            for son in reversed(graph.get(node , [])):
                stack.append(son)
                parent[son] = node 

    return None

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

print(dfs_optimized(graph, 'A', 'G'))  # Output: ['A', 'D', 'G']
