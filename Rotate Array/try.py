class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
      
        for i in range(0,k):
            nums.insert(0,nums[-1])	#move last to first index
            nums.pop(-1)			#pop last element
        print(nums)