class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert(node.right, key, value)
        else:
            # If the key already exists, update the value
            node.value = value

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        result = []
        if node:
            result = self._inorder_traversal(node.left)
            result.append((node.key, node.value))
            result += self._inorder_traversal(node.right)
        return result


bst = BinarySearchTree()
bst.insert(50, 'Value at 50')
bst.insert(30, 'Value at 30')
bst.insert(70, 'Value at 70')
bst.insert(20, 'Value at 20')
bst.insert(40, 'Value at 40')
bst.insert(60, 'Value at 60')
bst.insert(80, 'Value at 80')

print("In-order Traversal:", bst.inorder_traversal())
print("Search for key 30:", bst.search(30))
print("Search for key 90:", bst.search(90))  
