class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> 'int':
        sorted_nums = sorted(nums)
        sum=0
        
        for i in range(len(nums)):
            if i%2==0:
                sum +=sorted_nums[i]
        return sum