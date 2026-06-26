class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from itertools import combinations
        
        def area(p1, p2, p3):
            return abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            ) / 2.0
        
        max_area = 0.0
        
        for a, b, c in combinations(points, 3):
            max_area = max(max_area, area(a, b, c))
        
        return max_area
