class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hmap = {}
        res =[]
        
        for n in nums2:
            if n in hmap:
                hmap[n] +=1
            else:
                hmap[n] =1
        
        for n in nums1:
            if n in hmap and hmap[n]>0:
                res.append(n)
                hmap[n] -=1
        return res        