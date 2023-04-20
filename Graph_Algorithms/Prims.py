import heapq

def prim(graph, start):
   
    mst = {start: {}}
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        
        if to in mst:
            continue
        
        mst[frm][to] = cost
        mst[to] = mst.get(to, {})
        mst[to][frm] = cost
        
        for next_node, weight in graph[to].items():
            if next_node not in mst:
                heapq.heappush(edges, (weight, to, next_node))
    
    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

#test
mst = prim(graph, 'A')
print(mst)
