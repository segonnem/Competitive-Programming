from collections import deque, defaultdict

def bfs(capacity, source, sink, parent):
    visited = set([source])
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in capacity[current]:
            if neighbor not in visited and capacity[current][neighbor] > 0:  
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
                if neighbor == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    total_flow = 0
    parent = {}
    
    for u in capacity:
        for v in capacity[u]:
            if v not in capacity:
                capacity[v] = {}
            if u not in capacity[v]:
                capacity[v][u] = 0
    
    while bfs(capacity, source, sink, parent):
        
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        
        total_flow += path_flow
    
    return total_flow

graph = {
    'A': {'B': 10, 'C': 10},
    'B': {'C': 1, 'D': 10},
    'C': {'E': 10},
    'D': {'E': 10},
    'E': {}
}

source = 'A'
sink = 'E'
print("Le flot maximal est:", edmonds_karp(graph, source, sink))
