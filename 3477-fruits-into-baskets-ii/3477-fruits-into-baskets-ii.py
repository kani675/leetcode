class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n
        unplaced_count = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True  # Mark basket as used
                    placed = True
                    break  # Move to next fruit
            if not placed:
                unplaced_count += 1  # Couldn't place this fruit

        return unplaced_count

# Driver Code
# Example 1:
print(Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))  # Output: 1

# Example 2:
print(Solution().numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))  # Output: 0
