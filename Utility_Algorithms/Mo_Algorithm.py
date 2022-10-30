import math

class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

def mo_algorithm(arr, queries):

    block_size = int(math.sqrt(len(arr)))
    def query_sort(q):
        primary = q.l // block_size
        secondary = q.r if primary % 2 == 0 else -q.r
        return (primary, secondary)

    queries.sort(key=query_sort)
    current_l, current_r, freq, ans = 0, 0, {}, [0] * len(queries)

    def add(position, freq):
        element = arr[position]
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    def remove(position, freq):
        element = arr[position]
        if freq[element] == 1:
            del freq[element]
        else:
            freq[element] -= 1

    for query in queries:
        while current_l > query.l:
            current_l -= 1
            add(current_l, freq)
        while current_r <= query.r:
            add(current_r, freq)
            current_r += 1
        while current_l < query.l:
            remove(current_l, freq)
            current_l += 1
        while current_r > query.r + 1:
            current_r -= 1
            remove(current_r, freq)

        ans[query.idx] = len(freq)

    return ans


arr = [1, 1, 2, 1, 3, 4, 5, 2, 6, 6]
queries = [Query(0, 4, 0), Query(1, 3, 1), Query(2, 9, 2)]
results = mo_algorithm(arr, queries)

print("Results of queries:")
for result in results:
    print(result)
