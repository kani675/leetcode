from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_length = 0

        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[j][diff] = dp[i][diff] + 1 if diff in dp[i] else 2
                max_length = max(max_length, dp[j][diff])

        return max_length
