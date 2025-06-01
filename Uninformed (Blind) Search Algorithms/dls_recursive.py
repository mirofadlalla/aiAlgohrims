

def dls_recursive(node, goal, depth , path=None):
    """
    Perform Depth-Limited Search (DLS) recursively.

    :param node: The current node to explore.
    :param goal: The goal node to find.
    :param depth: The maximum depth to search.
    :return: The goal node if found, None otherwise.
    """
    if path == None:
        path = []

    path.append(node)
    if node == goal :
        return list(path)
    
    if depth <= 0:
        return None
    
    for son in graph.get(node, []):
        if son not in path:
            result = dls_recursive(son, goal, depth - 1, path)
            if result is not None:
                return result
    path.pop()  # backtrack
    return None
# Example graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}
# Example usage
print(dls_recursive('A', 'G', depth=2))  # None (too shallow)
print(dls_recursive('A', 'G', depth=3))  # ['A', 'D', 'G']
    