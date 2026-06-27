from collections import deque

class Solution:
    def isCompleteTree(self, root):
        queue = deque([root])
        end = False  # Flag to indicate if we have seen a null node.

        while queue:
            node = queue.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False  # Found a non-null node after a null node.
                queue.append(node.left)
                queue.append(node.right)

        return True  # Traversed without violations.
