def create_adjacency_matrix(graph):
    # Extract unique vertices and sort them
    vertices = sorted(graph.keys())
    vertex_indices = {vertex: idx for idx, vertex in enumerate(vertices)}
    V = len(vertices)
    
    # Create an adjacency matrix with all values set to infinity
    INF = float('inf')
    adj_matrix = [[INF] * V for _ in range(V)]
    
    # Set diagonal to 0 as the distance to itself is zero
    for i in range(V):
        adj_matrix[i][i] = 0
    
    for vertex in graph:
        for neighbor in graph[vertex]:
            weight = graph[vertex][neighbor]
            i, j = vertex_indices[vertex], vertex_indices[neighbor]
            adj_matrix[i][j] = weight

    return adj_matrix, vertices

def floyd_warshall(graph):
    weights, vertices = create_adjacency_matrix(graph)
    V = len(vertices)

    dist = [row[:] for row in weights]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist, vertices

graph = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 3: 5},
    3: {}
}

distances, vertices = floyd_warshall(graph)
print("Shortest distances between every pair of vertices:")
for i, v_i in enumerate(vertices):
    for j, v_j in enumerate(vertices):
        if distances[i][j] == float('inf'):
            print(f"From {v_i} to {v_j}: No Path")
        else:
            print(f"From {v_i} to {v_j}: {distances[i][j]}")
    print("")
