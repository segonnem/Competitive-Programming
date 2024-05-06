def tarjan(v, index, stack, indices, lowlinks, on_stack, adj_list, sccs):
    indices[v] = index
    lowlinks[v] = index
    index += 1
    stack.append(v)
    on_stack[v] = True

    for w in adj_list[v]:
        if indices[w] == -1:
            tarjan(w, index, stack, indices, lowlinks, on_stack, adj_list, sccs)
            lowlinks[v] = min(lowlinks[v], lowlinks[w])
        elif on_stack[w]:
            lowlinks[v] = min(lowlinks[v], indices[w])

    if lowlinks[v] == indices[v]:
        current_scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            current_scc.append(w)
            if w == v:
                break
        sccs.append(current_scc)

def add_implication(x, y, adj_list):
    adj_list[x].append(y)
    adj_list[y ^ 1].append(x ^ 1)

def add_clause(x, y, adj_list):
    add_implication(x ^ 1, y, adj_list)
    add_implication(y ^ 1, x, adj_list)

def solve_2_sat(num_variables, clauses):
    num_vertices = 2 * num_variables
    adj_list = [[] for _ in range(num_vertices)]
    indices = [-1] * num_vertices
    lowlinks = [-1] * num_vertices
    on_stack = [False] * num_vertices
    stack = []
    sccs = []

    for (x, y) in clauses:
        add_clause(x, y, adj_list)

    # Find all SCCs using Tarjan's algorithm
    for i in range(num_vertices):
        if indices[i] == -1:
            tarjan(i, 0, stack, indices, lowlinks, on_stack, adj_list, sccs)

    assignment = [False] * num_variables

    for scc in sccs:
        for v in scc:
            if v ^ 1 in scc:
                return None 
            assignment[v // 2] = v % 2 == 0

    return assignment


clauses = [(0, 2), (1, 3), (2, 1)] #refers to A B C D etc.
result = solve_2_sat(2, clauses)
print("Satisfiable" if result else "Unsatisfiable")
if result:
    print("Solution:", result)
