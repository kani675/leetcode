class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            
            i += 1
            j -= 1

        return -1
