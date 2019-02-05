class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        abin = int(a,2)
        bbin = int(b,2)
        return bin(abin+bbin)[2:]