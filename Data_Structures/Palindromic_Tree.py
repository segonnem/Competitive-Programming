class PalindromicTree:
    def __init__(self):
        self.nodes = [self.Node(-1), self.Node(0)]  # -1 -> imaginary node, 0 -> root with empty string
        self.size = 2
        self.s = []
        self.suffix = 1

    class Node:
        def __init__(self, length):
            self.length = length
            self.link = 0 
            self.next = {}  
            self.count = 0  # To count occurrences of the palindrome

    def get_link(self, v):
        while True:
            j = len(self.s) - self.nodes[v].length - 2
            if j >= 0 and self.s[j] == self.s[len(self.s) - 1]:
                break
            v = self.nodes[v].link
        return v

    def add_letter(self, c):
        self.s.append(c)
        pos = len(self.s) - 1
        current = self.get_link(self.suffix)

        if c in self.nodes[current].next:
            self.suffix = self.nodes[current].next[c]
            self.nodes[self.suffix].count += 1
            return self.size

        # Create new node
        self.suffix = self.size
        self.nodes.append(self.Node(self.nodes[current].length + 2))
        self.nodes[current].next[c] = self.size
        self.size += 1

        # Set the suffix link for the new node
        if self.nodes[self.suffix].length == 1:
            self.nodes[self.suffix].link = 1
            self.nodes[self.suffix].count = 1
            return self.size

        self.nodes[self.suffix].link = self.nodes[self.get_link(self.nodes[current].link)].next[c]
        self.nodes[self.suffix].count = 1
        return self.size

    def count_unique_palindromes(self):
        return sum(node.count for node in self.nodes[2:])

pal_tree = PalindromicTree()
test_string = "ababa"
for char in test_string:
    pal_tree.add_letter(char)

print(f"Total unique palindromes in '{test_string}':", pal_tree.count_unique_palindromes())
