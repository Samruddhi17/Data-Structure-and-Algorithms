class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        position ={}
        start =0
        maxlen =0
        
        
        for i, char in enumerate(s):
            if (char not in position or position[char]<start): #repeating char can be in new substring
                maxlen =max(maxlen,i+1-start) #len of substring
            else:
                start = position[char] +1 #new start
            
            position[char] =i
        return maxlen