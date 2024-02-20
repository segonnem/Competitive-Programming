from collections import deque, defaultdict

def hopcroft_karp(graph, left_vertices):

    def bfs():
        queue = deque()
        for v in left_vertices:
            if pair_U[v] == None:
                distances[v] = 0
                queue.append(v)
            else:
                distances[v] = float('inf')
        distances[None] = float('inf')  # Sentinel node
        while queue:
            u = queue.popleft()
            if distances[u] < distances[None]:
                for v in graph[u]:
                    if distances[pair_V[v]] == float('inf'):
                        distances[pair_V[v]] = distances[u] + 1
                        queue.append(pair_V[v])
        return distances[None] != float('inf')

    def dfs(u):
        if u is not None:
            for v in graph[u]:
                if distances[pair_V[v]] == distances[u] + 1:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True
            distances[u] = float('inf')
            return False
        return True

    pair_U = {u: None for u in left_vertices}  # Pairings for U
    pair_V = {v: None for u in left_vertices for v in graph[u]}  # Pairings for V
    matching = 0
    distances = {}

    while bfs():
        for u in left_vertices:
            if pair_U[u] == None:
                if dfs(u):
                    matching += 1
    return matching

graph = {
    'u1': {'v1': 1, 'v2': 1},
    'u2': {'v1': 1},
    'u3': {'v3': 1}
}

left_vertices = ['u1', 'u2', 'u3']
max_matching = hopcroft_karp(graph, left_vertices)
print("Maximum matching size:", max_matching)
