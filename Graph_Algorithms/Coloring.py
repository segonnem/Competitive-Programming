def color_graph(graph):
    colors = {}  # dictionary to store the colors assigned to each node
    for node in graph:
        available_colors = set(range(len(graph)))  # we assume the worst case: one color per node
        available_colors -= {colors.get(neigh) for neigh in graph[node] if neigh in colors}
        colors[node] = min(available_colors)
    return colors

graph = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'C': 1, 'D': 1},
    'C': {'A': 1, 'B': 1, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

coloring = color_graph(graph)
print("Graph Coloring:", coloring)
