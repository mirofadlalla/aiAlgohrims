import heapq

def UCS(graph , start , goal):

    visited = set()
    queue = [ ( 0 , [start] ) ]

    while queue :
        cost , path = heapq.heappop(queue)
        node = path[-1]

        if node == goal :
            return cost , path 
        

        if node not in visited :
            visited.add(node)
            for son , edge_cost in graph.get(node , []):
                if son not in visited :
                    new_path = path + [son] #this is the same as new_path = list(path) then new_path.append(son) but it creates a new list
                    heapq.heappush(queue , (cost+edge_cost , new_path)) #

    return None, []


# Graph represented as adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 4), ('D', 3)],
    'B': [('E', 2)],
    'C': [],
    'D': [('G', 2)],
    'E': [],
    'G': []
}

path, cost = UCS(graph, 'A', 'G')
print("Path:", path)   # Output: ['A', 'D', 'G']
print("Cost:", cost)   # Output: 5