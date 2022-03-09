class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  # Using 1-based index

    def update(self, index, value):
        """Add 'value' to index 'index'."""
        while index <= self.size:
            self.tree[index] += value
            index += index & -index  # Move index to the next position

    def query(self, index):
        """Compute the prefix sum of [1, index]."""
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index  # Move index to parent
        return sum

    def range_query(self, left, right):
        """Compute the sum of the range [left, right]."""
        return self.query(right) - self.query(left - 1)


ft = FenwickTree(10)
ft.update(1, 5)  
ft.update(2, 3)  
ft.update(3, 7) 


