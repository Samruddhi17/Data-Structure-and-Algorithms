class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res =[]
        hmap = {}
        
        for n in nums1:
            if n not in hmap:
                hmap[n] =1
        
        for n in nums2:
            if n in hmap and hmap[n]>0:
                res.append(n)
                hmap[n] =0
        return res        