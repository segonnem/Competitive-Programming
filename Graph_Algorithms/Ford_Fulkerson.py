from collections import deque, defaultdict

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in capacity[u]:  # Itérer sur les clés du dictionnaire (les sommets)
            cap = capacity[u][v]  # Accéder à la capacité comme valeur du dictionnaire
            if v not in visited and cap > 0:  # Vérifier la capacité résiduelle
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(capacity, source, sink):
    parent = {}
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):  # Utilisation directe du graphe sans transformation
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        # Mise à jour des capacités résiduelles du réseau
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] = capacity.get(v, {}).get(u, 0) + path_flow  # Ajouter la capacité inverse si nécessaire
            v = u
        
        max_flow += path_flow
    
    return max_flow

# Exemple de graphe utilisant un dictionnaire de dictionnaires
graph = {
    'A': {'B': 10, 'C': 5},
    'B': {'C': 15, 'D': 9},
    'C': {'D': 10, 'Sink': 10},
    'D': {'Sink': 10},
    'Sink': {}
}

source = 'A'
sink = 'Sink'

print("Le flot maximal est :", ford_fulkerson(graph, source, sink))

