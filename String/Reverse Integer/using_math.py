class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        rem_digits = abs(x) // imp to avoid overflow
        
        while rem_digits:
            res = res*10 + rem_digits%10
            rem_digits =rem_digits//10
            
        if res >= 2**31 or res <= -2**31:
            return 0
        else:
            return -res if x<0 else res