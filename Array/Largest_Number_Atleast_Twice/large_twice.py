class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        index =0
        
        for i in range(len(nums)):
            if nums[i]> max_num:
                max_num=nums[i]
                index =i
                
        for i in range(len(nums)):
            if i!=index:
                if nums[i]*2 > max_num:
                    return -1
        return index        