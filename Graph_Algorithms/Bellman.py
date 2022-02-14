def bellman_ford(graph, src):
    V = len(graph)
    dist = {vertex: float('Inf') for vertex in graph}
    dist[src] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u in graph:
            for v in graph[u]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Check for negative weight cycles
    for u in graph:
        for v in graph[u]:
            if dist[u] + graph[u][v] < dist[v]:
                print("Graph contains a negative weight cycle")
                return None  # Return None to indicate an issue

    return dist


graph = {
    0: {1: -1, 2: 4},
    1: {2: 3, 3: 2, 4: 2},
    2: {},
    3: {2: 5, 1: 1},
    4: {3: -3}
}

distances = bellman_ford(graph, 0)
if distances:
    print("Distance from source:")
    for vertex in distances:
        print(f"Vertex {vertex} : {distances[vertex]}")
