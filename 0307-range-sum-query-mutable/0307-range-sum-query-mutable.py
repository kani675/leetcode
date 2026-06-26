class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # Set value at leaf
        pos = index + self.n
        self.tree[pos] = val
        # Update parent nodes
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        l, r = left + self.n, right + self.n
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res
