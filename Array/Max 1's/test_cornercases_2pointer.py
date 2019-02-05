class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        ret_max =0
        now_max=0
             
        for i in range(len(nums)):
            if nums[i]==1:
                now_max +=1
                if (now_max > ret_max):
                    ret_max = now_max
            elif nums[i]==0:
                now_max =0
        return ret_max