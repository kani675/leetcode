import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a min-heap of the first k elements
        heap = nums[:k]
        heapq.heapify(heap)

        # For the rest of the elements, keep the k largest
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        # Root of the heap is the kth largest
        return heap[0]
