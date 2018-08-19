class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        
        if len(a)==1 or a[-2]*2 <=a[-1]:
            return nums.index(a[-1])
        else:
            return -1