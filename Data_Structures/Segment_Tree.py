class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)  # Segment tree array
        self.build(data)

    def build(self, data):
        
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, value):
        
        pos += self.n
        self.tree[pos] = value
        i = pos
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def range_query(self, l, r):
        l += self.n
        r += self.n + 1
        sum = 0
        # Loop to find the sum in the range
        while l < r:
            if l & 1:
                sum += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum

data = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(data)
print("Initial sum of range(1, 3):", seg_tree.range_query(1, 3))
seg_tree.update(1, 10)
print("Sum of range(1, 3) after updating index 1 to 10:", seg_tree.range_query(1, 3))
