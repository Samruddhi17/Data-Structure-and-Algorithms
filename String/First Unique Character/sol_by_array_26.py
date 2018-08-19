class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_c =[0]*26
        
        for i in range(len(s)):
            map_c[ord(s[i])-ord('a')] +=1
        
        for i in range(len(s)):
            if map_c[ord(s[i])-ord('a')]==1:
                return i
        return -1        