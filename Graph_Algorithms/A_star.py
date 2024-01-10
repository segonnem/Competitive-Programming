import heapq

def a_star_algorithm(graph, start, end, h):
    open_heap = []
    heapq.heappush(open_heap, (h(start), start))
    came_from = {start: None}
    g_score = {vertex: float('inf') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex: float('inf') for vertex in graph}
    f_score[start] = h(start)
    
    while open_heap:
        current_f, current = heapq.heappop(open_heap)
        
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor)
                heapq.heappush(open_heap, (f_score[neighbor], neighbor))
    
    return False

def heuristic(node, goal):
    return 0 #dijkstra


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 2},
    'F': {}
}

# Example usage
path = a_star_algorithm(graph, 'A', 'F', lambda x: heuristic(x, 'F'))
print("Path from A to F:", path)
