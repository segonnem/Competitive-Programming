def find(component, vertex):
    if component[vertex] != vertex:
        component[vertex] = find(component, component[vertex])
    return component[vertex]

def union(component, rank, u, v):
    root_u = find(component, u)
    root_v = find(component, v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            component[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            component[root_u] = root_v
        else:
            component[root_v] = root_u
            rank[root_u] += 1

def boruvka(graph):

    component = {vertex: vertex for vertex in graph}
    rank = {vertex: 0 for vertex in graph}
    mst = {vertex: {} for vertex in graph}
    mst_weight = 0

    num_components = len(graph)
    while num_components > 1:
        
        cheapest = {}
        
        for vertex in graph:
            for adj, weight in graph[vertex].items():
                u = find(component, vertex)
                v = find(component, adj)
                if u != v:
                    if u not in cheapest or cheapest[u][0] > weight:
                        cheapest[u] = (weight, vertex, adj)

        
        for u, (weight, v1, v2) in cheapest.items():
            u = find(component, v1)
            v = find(component, v2)
            if u != v:
                mst[v1][v2] = weight
                mst[v2][v1] = weight
                mst_weight += weight
                union(component, rank, u, v)
                num_components -= 1

    return mst, mst_weight

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

#test Borukva
mst, mst_weight = boruvka(graph)
print("MST:", mst)
print("Total weight of MST:", mst_weight)
