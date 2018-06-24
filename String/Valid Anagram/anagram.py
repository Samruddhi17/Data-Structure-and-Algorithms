from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cs = Counter(s)
        ct = Counter(t)
        
        if cs == ct:
            return True
        else:
            return False