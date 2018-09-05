class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre =''
        if not strs:
            return pre
        
        low_prefix =min(strs) #least prefix word - flight
        max_prefix =max(strs) #max prefix word - flower
  
        
        if not low_prefix or not max_prefix:
            return pre
        
        for i,v in enumerate(low_prefix):
            if max_prefix[i]!=low_prefix[i]:
                return pre
            else:
                pre +=max_prefix[i]
        return pre