class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = list(set(nums))
        print (set_nums)
        if len(set_nums) == len(nums):
            return False
        else:
            return True