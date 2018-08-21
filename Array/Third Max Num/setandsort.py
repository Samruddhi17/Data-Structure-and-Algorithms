class Solution(object):
    def thirdMax(self, nums):   
        set_n = list(set(nums))
        sort_n = list(sorted(set_n))
        
        if len(sort_n) >2:
            return sort_n[len(sort_n)-3]
        else:
            return sort_n[-1]
            
        
        