class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2=max3 = -sys.maxsize-1
        
        
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            else:
                if num > max1:
                    max1,max2,max3 = num,max1,max2
                elif num > max2:
                    max2,max3 = num,max2
                elif num > max3:
                    max3 = num
           
        if max3 != -sys.maxsize-1:
            return max3
        else:
            return max1
                