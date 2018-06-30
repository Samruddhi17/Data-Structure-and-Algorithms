class Solution:
    def reverse(self, x):
        x_str = str(abs(x))[::-1]
        
        if int(x_str) >= 2**31 or int(x_str)<=-2**31:
            return 0
        else:
            return (int(x_str) if x>0 else -(int(x_str)))