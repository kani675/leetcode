from collections import defaultdict

class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        xor_subtree = [0] * n
        tin = [0] * n
        tout = [0] * n
        time = [0]

        def dfs(u, parent):
            time[0] += 1
            tin[u] = time[0]
            xor_subtree[u] = nums[u]
            for v in tree[u]:
                if v != parent:
                    dfs(v, u)
                    xor_subtree[u] ^= xor_subtree[v]
            time[0] += 1
            tout[u] = time[0]

        dfs(0, -1)

        def isAncestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        total_xor = xor_subtree[0]
        res = float('inf')

        nodes = [i for i in range(1, n)]
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                u, v = nodes[i], nodes[j]

                if isAncestor(u, v):
                    comp1 = xor_subtree[v]
                    comp2 = xor_subtree[u] ^ xor_subtree[v]
                    comp3 = total_xor ^ xor_subtree[u]
                elif isAncestor(v, u):
                    comp1 = xor_subtree[u]
                    comp2 = xor_subtree[v] ^ xor_subtree[u]
                    comp3 = total_xor ^ xor_subtree[v]
                else:
                    comp1 = xor_subtree[u]
                    comp2 = xor_subtree[v]
                    comp3 = total_xor ^ xor_subtree[u] ^ xor_subtree[v]

                vals = [comp1, comp2, comp3]
                res = min(res, max(vals) - min(vals))

        return res
