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
    
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children, get the inorder successor
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current



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
print("Height of the tree:", bst.height())

bst.delete(30) 
bst.delete(70)
bst.delete(50)  
print("In-order Traversal after deleting the root (50):", bst.inorder_traversal())
