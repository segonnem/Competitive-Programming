
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item]) 
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal's algorithm implementation using the dictionary representation of the graph
def kruskal(graph):
    # Initialize union-find structure
    uf = UnionFind(len(graph))
    mst = []  # To store the edges of the Minimum Spanning Tree (MST)
    mst_weight = 0  # Total weight of all edges in the MST

    edges = []
    for vertex in graph:
        for edge in graph[vertex]:
            if (edge[0], vertex, edge[1]) not in edges and (vertex, edge[0], edge[1]) not in edges:
                edges.append((vertex, edge[0], edge[1]))

    edges.sort(key=lambda e: e[2])

    for edge in edges:
        vertex1, vertex2, weight = edge
        # Check if the current edge forms a cycle with the MST formed so far
        if uf.find(vertex1) != uf.find(vertex2): 
            mst.append(edge)  
            mst_weight += weight  
            uf.union(vertex1, vertex2) 
    
    return mst, mst_weight