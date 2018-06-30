class Solution:
       def twoSum(self, nums, target):
            h_table ={}
            for i in range(len(nums)):
                if nums[i] in h_table:
                    return(i,h_table.get(nums[i]))
                else:
                    h_table[target-nums[i]] =i