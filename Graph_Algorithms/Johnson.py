import heapq

def bellman_ford(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Detect negatives circles
    for u in graph:
        for v in graph[u]:
            if dist[u] + graph[u][v] < dist[v]:
                raise ValueError("Le graphe contient un cycle de poids négatif")

    return dist

def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v in graph[u]:
            new_dist = dist[u] + graph[u][v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist

def johnson(graph):
    
    graph[0] = {v: 0 for v in graph if v != 0}
    
    h = bellman_ford(graph, 0)
    del graph[0]
    
    for u in graph:
        for v in graph[u]:
            graph[u][v] += h[u] - h[v]

    # Application of Dijkstra 
    dist_matrix = {}
    for u in graph:
        dist_matrix[u] = dijkstra(graph, u)
        for v in dist_matrix[u]:
            dist_matrix[u][v] += h[v] - h[u]  

    return dist_matrix

graph = {
    1: {2: 3, 3: 8, 5: -4},
    2: {4: 1, 5: 7},
    3: {2: 4},
    4: {1: 2, 3: -5},
    5: {4: 6}
}

all_pairs_shortest_path = johnson(graph)
print("Distances entre toutes les paires de sommets:")
for start in all_pairs_shortest_path:
    print(f"Depuis {start}: {all_pairs_shortest_path[start]}")
