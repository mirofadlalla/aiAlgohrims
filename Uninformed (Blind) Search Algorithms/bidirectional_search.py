# How It Works (Steps):
# Initialize two queues:

# queue_start from start node

# queue_goal from goal node

# Each has its own visited and parent dictionary.

# Alternate expanding nodes from both directions.

# When a node appears in both visited sets, the searches have met.

# Reconstruct the full path by combining paths from both searches.

from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Initialize
    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        # Expand forward
        result = expand_layer(graph, queue_start, visited_start, visited_goal)
        if result:
            return result

        # Expand backward
        result = expand_layer(graph, queue_goal, visited_goal, visited_start)
        if result:
            return result

    return None  # No path found

def expand_layer(graph, queue, visited, other_visited):
    current = queue.popleft()

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)

            if neighbor in other_visited:
                # Reconstruct path
                return build_path(visited, other_visited, neighbor)

    return None

def build_path(visited_start, visited_goal, meeting_point):
    # Build path from start to meeting point
    path_start = []
    node = meeting_point
    while node:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    # Build path from meeting point to goal
    path_goal = []
    node = visited_goal[meeting_point]
    while node:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start + path_goal


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

print(bidirectional_search(graph, 'A', 'G'))  
# Output (one valid path): ['A', 'C', 'F', 'G']
