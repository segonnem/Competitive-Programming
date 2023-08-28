def topological_sort(graph):
    visited = set()  # Set to keep track of visited nodes
    stack = []  # Stack to store the order of nodes

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]


graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

order = topological_sort(graph)
print("Topological Order:")
print(order)
