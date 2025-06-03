import heapq

def reconstrate_pah(start , node , parent): # we say that it me want to find a path not from root only but somewehre in gaph so that wee pass the goal
    path = []
    #path.append(goal)  # Add the goal node to the path
    while node is not None and start != node : # we can only use node is not None becuz the parent of the start node is always None even if the start node is the goal node
        path.append(node)
        node = parent[node]

    path.append(start)  # Add the start node to the path

    

    return path[::-1]


def greedy(graph , start , goal , heuristic):

    path = [ ( heuristic , start)] # using a tuple (heuristic value, node) to prioritize nodes based on heuristic value
    heapq.heapify(path)  # Convert the list into a heap in-place
    parent = {start : None}

    while path :
        _ , node = heapq.heappop(path)

        if  node == goal :
            return reconstrate_pah(start , goal , parent)

        for son in graph.get(node , []):
            if son not in parent :
                heapq.heappush(path , (heuristic[son] , son)) 
                parent[son] = node


    return None  # No path found
# Example heuristic function
heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 0,
        'G': 0
    }

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'G'],
    'E': ['B'],
    'G': ['D']
}

# Example usage
start = 'A'
goal = 'G'
path = greedy(graph, start, goal, heuristics)
print("Path from", start, "to", goal, ":", path)  # Output: Path from A to G : ['A', 'C', 'D', 'G']
