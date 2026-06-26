class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[0]]  # Base case: 1x1 grid
        
        prev = self.specialGrid(n - 1)  # smaller special grid
        size = 2 ** (n - 1)
        total = 2 ** (2 * (n - 1))  # numbers in one quadrant
        grid = [[0] * (2 * size) for _ in range(2 * size)]
        
        # Fill quadrants with appropriate offsets
        for i in range(size):
            for j in range(size):
                # Top-right quadrant
                grid[i][j + size] = prev[i][j]  
                # Bottom-right quadrant
                grid[i + size][j + size] = prev[i][j] + total  
                # Bottom-left quadrant
                grid[i + size][j] = prev[i][j] + 2 * total  
                # Top-left quadrant
                grid[i][j] = prev[i][j] + 3 * total  
        
        return grid
