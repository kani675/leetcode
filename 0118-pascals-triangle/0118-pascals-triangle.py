class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Start with an empty list to store all rows
        triangle = []

        for i in range(numRows):
            # Create a new row with 1s; row i has i+1 elements
            row = [1] * (i + 1)
            
            # Fill in the middle elements (from index 1 to i-1)
            for j in range(1, i):
                # Sum the two elements directly above from the previous row
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle
