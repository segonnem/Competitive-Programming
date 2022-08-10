class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _zig(self, x):
        p = x.parent
        if p.left == x:
            # Right rotation
            p.left = x.right
            if x.right:
                x.right.parent = p
            x.right = p
        else:
            # Left rotation
            p.right = x.left
            if x.left:
                x.left.parent = p
            x.left = p
        x.parent = p.parent
        p.parent = x
        if x.parent:
            if x.parent.left == p:
                x.parent.left = x
            else:
                x.parent.right = x
        else:
            self.root = x
        self._update(p)
        self._update(x)

    def _splay(self, x):
        while x.parent:
            p = x.parent
            gp = p.parent
            if gp:
                self._zig(p if (gp.left == p) == (p.left == x) else x)
            self._zig(x)
        self.root = x

    def _update(self, x):
        # This function updates any additional metadata on the node x
        pass

    def insert(self, key):
        node, parent = self.root, None
        while node:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        new_node = Node(key)
        new_node.parent = parent
        if parent:
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
        else:
            self.root = new_node
        self._splay(new_node)

    def find(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                self._splay(node)
                return node
        return None

splay_tree = SplayTree()
splay_tree.insert(10)
splay_tree.insert(20)
splay_tree.insert(30)
found_node = splay_tree.find(20)
if found_node:
    print("Found:", found_node.key)
else:
    print("Not found")
found_node = splay_tree.find(20) #quick





