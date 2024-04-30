def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def is_cycle_undirected(graph):
    parent = {}
    rank = {}

    for vertex in graph:
        parent[vertex] = vertex
        rank[vertex] = 0

    for u in graph:
        for v in graph[u]:
            if u < v:  # Ensure each edge is only considered once
                uroot = find(parent, u)
                vroot = find(parent, v)
                if uroot == vroot:
                    return True
                union(parent, rank, uroot, vroot)
    return False


graph = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'D': 1},
    'C': {'A': 1, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

print("Cycle Detected" if is_cycle_undirected(graph) else "No Cycle Detected")




''' NOW use DFS'''

def is_cyclic_util(v, visited, rec_stack, graph):
    visited[v] = True
    rec_stack[v] = True

    for neighbour in graph[v]:
        if not visited[neighbour]:
            if is_cyclic_util(neighbour, visited, rec_stack, graph):
                return True
        elif rec_stack[neighbour]:
            return True

    rec_stack[v] = False
    return False

def is_cyclic(graph):
    visited = {v: False for v in graph}
    rec_stack = {v: False for v in graph}

    for node in graph:
        if not visited[node]:
            if is_cyclic_util(node, visited, rec_stack, graph):
                return True
    return False

# Example graph
directed_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['B']
}

print("Cycle Detected" if is_cyclic(directed_graph) else "No Cycle Detected")
