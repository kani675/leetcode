class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)

    def popcount_depth(self, x):
        depth = 0
        while x != 1:
            x = bin(x).count('1')
            depth += 1
        return depth

    def build(self, node, l, r, arr):
        if l == r:
            counts = [0] * 6
            d = self.popcount_depth(arr[l])
            counts[d] = 1
            self.tree[node] = counts
            return
        mid = (l + r) // 2
        self.build(node*2, l, mid, arr)
        self.build(node*2+1, mid+1, r, arr)
        self.tree[node] = [self.tree[node*2][i] + self.tree[node*2+1][i] for i in range(6)]

    def query(self, node, l, r, ql, qr, k):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node][k]
        mid = (l + r) // 2
        return self.query(node*2, l, mid, ql, qr, k) + self.query(node*2+1, mid+1, r, ql, qr, k)

    def update(self, node, l, r, idx, val):
        if l == r:
            counts = [0] * 6
            d = self.popcount_depth(val)
            counts[d] = 1
            self.tree[node] = counts
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(node*2, l, mid, idx, val)
        else:
            self.update(node*2+1, mid+1, r, idx, val)
        self.tree[node] = [self.tree[node*2][i] + self.tree[node*2+1][i] for i in range(6)]

class Solution(object):
    def popcountDepth(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        st = SegmentTree(nums)
        answer = []

        for q in queries:
            if q[0] == 1:
                # Query: [1, l, r, k]
                _, l, r, k = q
                answer.append(st.query(1, 0, st.n - 1, l, r, k))
            else:
                # Update: [2, idx, val]
                _, idx, val = q
                st.update(1, 0, st.n - 1, idx, val)

        return answer
