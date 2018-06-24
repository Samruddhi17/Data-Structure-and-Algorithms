from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cs = Counter(nums)
        for n in nums:
            if cs[n] == 1:
                return n