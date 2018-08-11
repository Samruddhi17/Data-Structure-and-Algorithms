class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) ==1:
            min_nums=nums[0]
            return min_nums
        min_nums = nums[0]
        for i in range (1,len(nums)):
            if min_nums > nums[i]:
                min_nums = nums[i]
        return min_nums           