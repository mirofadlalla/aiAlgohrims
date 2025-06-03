
# A* Algorithm Steps
# Start from the initial node.

# Add it to a priority queue with priority f(n) = g(n) + h(n).

# While the queue is not empty:

# Pop the node with the lowest f(n).

# If it’s the goal, reconstruct the path.

# Otherwise, expand its neighbors.

# For each neighbor, update g(n) and f(n) and add to queue if it’s a better path.

# Graph:
#     A
#    / \
#  B(1) C(3)
#    \   \
#    D(1) G(2)
#     \ /
#      G

# Heuristic (h):
# G: 0
# D: 1
# B: 4
# C: 2
# A: 5

import heapq

def reconstrate_path(start , node , parent) :
    path = []

    while node is not None :
        path.append(node)
        node = parent[node]

    return path[::-1]

def a_star(graph , start , goal , heaurstic):

    path = [( 0 + heaurstic[start] , start )] # ( f(n) , node ) => f(n) = g(n) + h(n) 
    heapq.heapify(path)
    parent = {start : None} # reconstrate_path
    cost_so_far = {start : 0} # g(n) calc the cost from the start node to the current node


    while path :
        _ , node = heapq.heappop(path)

        if node == goal :
            return reconstrate_path(start , goal , parent)


        for son , cost in graph.get(node , []):
            new_cost = cost_so_far[node] + cost # if we have path A->B->D and with cost = 5 from start to D and there is another path from A to D by C => A->C->D and the cost from A to C is 3 
            # new_cost < cost_so_far[son] this conditon ensures to not choose the goal path but the best goal path 
            if son not in parent or new_cost < cost_so_far[son] :
                cost_so_far[son] = new_cost # edit or overwiter the D cost from 5 to 4 
                f_n = cost + heaurstic[son]
                heapq.heappush(path , (f_n , son))
                parent[son] = node 
    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 1,
    'G': 0
}

start = 'A'
goal = 'G'
path = a_star(graph, start, goal, heuristic)
print("Path from", start, "to", goal, ":", path)  # Output: Path from A to G : ['A', 'B', 'D', 'G']
