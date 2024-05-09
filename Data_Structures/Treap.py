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

# test + priority
treap = Treap()

keys_with_priorities = [(5, 20), (3, 30), (8, 10), (1, 40), (7, 25)]
for key, priority in keys_with_priorities:
    treap.insert(key, priority)

print("Inorder traversal of the Treap after specific priorities:", treap.inorder())

# Test with sequential keys to check BST properties
sequential_keys = [10, 20, 30, 40, 50]
for key in sequential_keys:
    treap.insert(key)

print("Inorder traversal of the Treap with sequential keys:", treap.inorder())

