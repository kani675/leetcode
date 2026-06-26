class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        l = len(nums[0])
        k = 2 ** l  -1

        while k >= 0:
            x = bin(k)[2:].zfill(l)   # remove '0b' and pad with zeros
            if x not in nums:
                return x
            k -= 1
