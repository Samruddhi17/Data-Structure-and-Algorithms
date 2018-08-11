class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        start,middle,end = 0,(length-1)//2, length-1
        
        while True:
            if middle==start:
                return(min(nums[start],nums[end]))
            elif nums[end] < nums[middle]:
                start = middle
            elif nums[middle] < nums[end]:
                end = middle
            middle = (start+end)//2
                