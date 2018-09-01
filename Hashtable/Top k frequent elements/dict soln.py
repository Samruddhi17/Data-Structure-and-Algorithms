class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        sorted_dict =[]
        res = []
        
        for n in nums:
            dict1[n] = dict1.get(n,0) +1  #increase count by 1
        
        sorted_dict =sorted(dict1, key=dict1.get,reverse=True) #sort by value and reverse
        
        for i in range(k):
            res.append(sorted_dict[i])
        return res
        
        