class BTreeNode:
    def __init__(self, t):
        self.keys = []
        self.children = []
        self.leaf = True
        self.t = t  # Minimum degree 

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def search(self, k, x=None):
        if isinstance(x, None):
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return x, i
        if x.leaf:
            return None
        else:
            return self.search(k, x.children[i])

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(t)
        z.leaf = y.leaf
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys.pop())

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            s = BTreeNode(self.t)
            self.root = s
            s.children.insert(0, root)
            s.leaf = False
            self.split_child(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)
