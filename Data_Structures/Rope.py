class RopeNode:
    def __init__(self, data):
        self.data = data
        self.weight = len(data) if data is not None else 0
        self.left = None
        self.right = None

class Rope:
    def __init__(self, string):
        self.root = RopeNode(string)

    def _concat(self, root1, root2):
        new_root = RopeNode(None)
        new_root.left = root1
        new_root.right = root2
        new_root.weight = root1.weight if root1 else 0
        return new_root

    def concat(self, rope):
        if rope.root:
            self.root = self._concat(self.root, rope.root)

    def _report(self, node, i, j):
        if node is None or i >= j:
            return ""
        if node.left is None and node.right is None:  # leaf node
            return node.data[i:j]
        mid = node.weight
        if j <= mid:
            return self._report(node.left, i, j)
        elif i >= mid:
            return self._report(node.right, i - mid, j - mid)
        else:
            return self._report(node.left, i, mid) + self._report(node.right, 0, j - mid)

    def report(self, i, j):
        return self._report(self.root, i, j)

rope1 = Rope("Hello ")
rope2 = Rope("World!")
rope1.concat(rope2)
print("Concatenated string:", rope1.report(0, 11))

