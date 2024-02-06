def tarjan(graph):
    index = 0  
    stack = []  
    indices = {}  
    lowlink = {}  
    result = []  # List to hold the strongly connected components

    def strongconnect(vertex):
        nonlocal index
        indices[vertex] = lowlink[vertex] = index
        index += 1
        stack.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlink[vertex] = min(lowlink[vertex], lowlink[neighbor])
            elif neighbor in stack:
                lowlink[vertex] = min(lowlink[vertex], indices[neighbor])

        
        if lowlink[vertex] == indices[vertex]:
            connected_component = []

            while True:
                w = stack.pop()
                connected_component.append(w)
                if w == vertex:
                    break

            result.append(connected_component)

    # Call the strongconnect function for every vertex not yet visited
    for v in graph:
        if v not in indices:
            strongconnect(v)

    return result

graph = {
    1: [2],
    2: [3],
    3: [1, 4],
    4: [5],
    5: [6],
    6: [4, 7],
    7: []
}

scc = tarjan(graph)
print("Strongly connected components:")
for component in scc:
    print(component)
