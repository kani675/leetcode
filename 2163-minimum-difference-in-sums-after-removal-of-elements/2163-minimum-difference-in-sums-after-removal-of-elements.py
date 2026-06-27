import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3
        total = len(nums)

        # Left to right: track n smallest elements (max heap)
        left_heap = []
        left_sum = 0
        prefix = [0] * total

        for i in range(total):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)  # pop removes largest (remember -num)
            if len(left_heap) == n:
                prefix[i] = left_sum

        # Right to left: track n largest elements (min heap)
        right_heap = []
        right_sum = 0
        suffix = [0] * total

        for i in range(total - 1, -1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)
            if len(right_heap) == n:
                suffix[i] = right_sum

        # Find min difference over all valid split points
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = prefix[i] - suffix[i + 1]
            min_diff = min(min_diff, diff)

        return min_diff
