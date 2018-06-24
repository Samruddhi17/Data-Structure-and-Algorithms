class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        for a in s:
            if (a.isalnum()) == True:
                list1.append(a.lower())
        
        list2 = list(reversed(list1))
        
        if list1 == list2:
            return True
        else:
            return False