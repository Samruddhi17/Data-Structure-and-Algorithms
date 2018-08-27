class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x1 = str(bin(x))[2:]    #convert to binary
        y1 = str(bin(y))[2:]
        
        xr = bin(int(x1,2)^int(y1,2)) #xor to find different bits
        xrs = str(xr)
        return xrs.count('1')       #count 1's