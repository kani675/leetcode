class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            # Shift result left to make space for the next bit
            result <<= 1
            # Add the least significant bit of n to result
            result |= (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return result
