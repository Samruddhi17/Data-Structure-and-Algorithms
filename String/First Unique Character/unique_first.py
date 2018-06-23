from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = list(s)
        new_ls = Counter(ls)    #count all letters
        print(new_ls)
        
        for l in range(0,len(s)):
            if new_ls[s[l]] == 1:
                return l
        return -1