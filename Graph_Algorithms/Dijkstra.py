import heapq

def dijkstra(graph, src):
    V = len(graph)
    
    dist = {vertex: float('Inf') for vertex in graph}
    dist[src] = 0

    priority_queue = [(0, src)]  # (distance, vertex)

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > dist[current_vertex]:
            continue

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist

graph = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 3: 5},
    3: {}
}

distances = dijkstra(graph, 0)
print("Distance from source:")
for vertex in distances:
    print(f"Vertex {vertex} : {distances[vertex]}")
