class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None  # Failure link
        self.output = []

class AhoCorasick:
    def __init__(self, keywords):
        self.root = TrieNode()
        self.build_trie(keywords)
        self.build_failure_links()

    def build_trie(self, keywords):
        for keyword in keywords:
            current = self.root
            for char in keyword:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.output.append(keyword)

    def build_failure_links(self):
        from collections import deque
        queue = deque()
        
        # Initial setting of failure links for first level children of root
        for char, node in self.root.children.items():
            node.fail = self.root
            queue.append(node)
        
        while queue:
            current = queue.popleft()

            # Set the failure link for each child
            for char, child_node in current.children.items():
                queue.append(child_node)
                fail = current.fail
                while fail is not None and char not in fail.children:
                    fail = fail.fail
                child_node.fail = fail.children[char] if fail and char in fail.children else self.root
                if child_node.fail:
                    child_node.output.extend(child_node.fail.output)

    def search(self, text):
        current = self.root
        results = []
        for index, char in enumerate(text):
            while current is not self.root and char not in current.children:
                current = current.fail
            if char in current.children:
                current = current.children[char]
            else:
                continue

            if current.output:
                for pattern in current.output:
                    results.append((index - len(pattern) + 1, pattern))

        return results



