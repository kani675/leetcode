class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # Add 1 if the last bit is set
            n >>= 1         # Shift right to check the next bit
        return count
