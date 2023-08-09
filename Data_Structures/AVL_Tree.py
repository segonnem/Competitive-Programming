class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def update_height(self, node):
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.balance_factor(root)

        
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
