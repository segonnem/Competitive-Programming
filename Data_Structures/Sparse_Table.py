import math

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self.st = [[0] * (int(math.log2(self.n)) + 1) for _ in range(self.n)]

        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        for i in range(self.n):
            self.st[i][0] = arr[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, l, r):
        j = self.log[r - l + 1]
        return min(self.st[l][j], self.st[r - (1 << j) + 1][j])


arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
sparse_table = SparseTable(arr)
print("Minimum of range [0, 4]:", sparse_table.query(0, 4))
print("Minimum of range [4, 7]:", sparse_table.query(4, 7))
print("Minimum of range [7, 8]:", sparse_table.query(7, 8))
