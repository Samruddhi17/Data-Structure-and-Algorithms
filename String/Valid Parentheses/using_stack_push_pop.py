class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in range(len(s)):
            if (s[i] == '(') or (s[i] == '[') or (s[i] == '{'):
                stack.append(s[i])
            elif stack:
                if s[i] == ')':
                    popped =stack.pop(-1)
                    if popped =='(':
                        continue
                    else:
                        return False
                if s[i] == '}':
                    popped =stack.pop(-1)
                    if popped =='{':
                        continue
                    else:
                        return False
                if s[i] == ']':
                    popped =stack.pop(-1)
                    if popped =='[':
                        continue
                    else:
                        return False
            else:
                return False
        if not stack:
            return True
        else:
            return False