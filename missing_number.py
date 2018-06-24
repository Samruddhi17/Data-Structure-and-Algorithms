class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        print(range(length+1))
        print(sum(nums))
        return sum(range(length+1)) - sum(nums)