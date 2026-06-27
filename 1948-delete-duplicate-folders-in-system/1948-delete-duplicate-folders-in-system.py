from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.name = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = TrieNode()
        
        # Build folder tree
        for path in paths:
            node = root
            for folder in path:
                node = node.children[folder]
                node.name = folder

        subtree_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for child in sorted(node.children.values(), key=lambda x: x.name):
                items.append("{}({})".format(child.name, serialize(child)))
            subtree_str = "".join(items)
            subtree_map[subtree_str].append(node)
            return subtree_str

        serialize(root)

        # Mark all duplicate subtrees
        for nodes in subtree_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        # Collect remaining folders
        result = []
        def dfs(node, path):
            for folder, child in node.children.items():
                if not child.is_deleted:
                    path.append(folder)
                    result.append(path[:])
                    dfs(child, path)
                    path.pop()

        dfs(root, [])
        return result
