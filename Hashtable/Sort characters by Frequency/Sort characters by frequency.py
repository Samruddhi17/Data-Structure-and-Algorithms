from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = Counter(s)
        op =[]
        s_sorted = list(sorted(s,key=s.get,reverse=True))
        
        for l in s_sorted:
            op +=[l]*s[l]
        return(''.join(op))
        