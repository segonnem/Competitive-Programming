class AhoCorasick:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.fail = None 
            self.output = []  

    def __init__(self, patterns):
        self.root = self.TrieNode()
        self.patterns = patterns
        self._build_trie()
        self._build_failure_links()

    def _build_trie(self):
        # Build the trie for the set of patterns
        for index, pattern in enumerate(self.patterns):
            node = self.root
            for symbol in pattern:
                if symbol not in node.children:
                    node.children[symbol] = self.TrieNode()
                node = node.children[symbol]
            node.output.append(index)

    def _build_failure_links(self):
        # Build failure links using BFS
        from collections import deque
        queue = deque()
        for node in self.root.children.values():
            node.fail = self.root
            queue.append(node)
        while queue:
            current_node = queue.popleft()

            for symbol, child_node in current_node.children.items():
                queue.append(child_node)
                fail_node = current_node.fail
                while fail_node is not None and symbol not in fail_node.children:
                    fail_node = fail_node.fail
                child_node.fail = fail_node.children[symbol] if fail_node else self.root
                if child_node.fail:
                    child_node.output.extend(child_node.fail.output)

    def search(self, text):
        node = self.root
        results = []
        for i, symbol in enumerate(text):
            while node is not None and symbol not in node.children:
                node = node.fail
            if node is None:
                node = self.root
                continue
            node = node.children[symbol]
            if node.output:
                for pattern_idx in node.output:
                    start_idx = i - len(self.patterns[pattern_idx]) + 1
                    results.append((start_idx, self.patterns[pattern_idx]))
        return results


patterns = ['he', 'she', 'his', 'hers']
text = 'ahishers'
ahocorasick = AhoCorasick(patterns)
found_patterns = ahocorasick.search(text)
print("Found patterns:", found_patterns) #perform in O(n+m) instead of naive O(nm)

