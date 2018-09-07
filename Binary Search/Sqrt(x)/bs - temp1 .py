class Solution(object):
    def mySqrt(self, x):
        """
        Return the truncated square root of x 
        AKA
        Return the max integer such that integer**2 <= x

        :type x: int
        :rtype: int
        """
        low, hi = 0, x
        
        # Binary search for the truncated square root of x
        # Loop invariant: low is always +1 index from last valid square (mid**2 <= x)
        while low <= hi:
            mid = (low + hi)/2
            if mid**2 <= x:
                low = mid + 1
            else:
                hi = mid - 1
        
        return low -1