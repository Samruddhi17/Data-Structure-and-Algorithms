class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pairs = {'}':'{', ')':'(',']':'['}
        vals = pairs.values()
        
        for i in s:
            if i in vals:
                stack.append(i)
            else:
                if stack:
                    if pairs[i] != stack.pop():
                        return False
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False