
def dfs(graph, start, goal):
    
    visited  = set()
    stack = [[start]]

    while stack :
        print(stack) # for trace 
        path =  stack.pop()
        node = path[-1]

        if node == goal :
            return path 
        
        if node not in visited :
            visited.add(node)
            sonsOfCurrentNode = reversed(graph[node]) # reverse to get the same order as BFS
            # sonsOfCurrentNode = graph[node] # if you want to keep the original order but then u have to use path =  stack.pop(0)
            for son in sonsOfCurrentNode :
                new_path = list(path)
                new_path.append(son)
                stack.append(new_path)

    
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

print(dfs(graph, 'A', 'G'))  # Output: ['A', 'D', 'G']


set_test = (1,"omar")

print(set_test)

id , name = set_test
print(id)
print(name)