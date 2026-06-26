import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Create all events
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # start of building
            events.append((right, 0, 0))           # end marker

        # Step 2: Sort events by x-coordinate, then by height
        events.sort()

        result = []
        # Max-heap for active buildings (height, end)
        heap = [(0, float('inf'))]  # ground level
        prev_max = 0

        for x, neg_height, right in events:
            # Remove buildings that are ended
            while heap[0][1] <= x:
                heapq.heappop(heap)
            # Add new building
            if neg_height != 0:
                heapq.heappush(heap, (neg_height, right))

            # Current max height
            curr_max = -heap[0][0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
