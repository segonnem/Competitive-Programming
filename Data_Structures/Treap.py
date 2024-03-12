import random

class Node:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority if priority else random.randint(1, 100)
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _insert(self, node, key, priority):
        if node is None:
            return Node(key, priority)
        elif key < node.key:
            node.left = self._insert(node.left, key, priority)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, priority)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        return node

    def insert(self, key, priority=None):
        self.root = self._insert(self.root, key, priority)

    def _inorder(self, node):
        result = []
        if node:
            result += self._inorder(node.left)
            result.append(node.key)
            result += self._inorder(node.right)
        return result

    def inorder(self):
        return self._inorder(self.root)

# Test code for Treap
treap = Treap()
keys = [5, 3, 8, 1, 7]
for key in keys:
    treap.insert(key)

print("Inorder traversal of the Treap:", treap.inorder())
