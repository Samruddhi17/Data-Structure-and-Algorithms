class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        hashmap ={}
        count =0
        
        if not J or not S:
            return 0
        
        for stone in J:
            if stone not in hashmap:
                hashmap[stone]=1
        
        for st in S:
            if st in hashmap:
                count+=1
        return count