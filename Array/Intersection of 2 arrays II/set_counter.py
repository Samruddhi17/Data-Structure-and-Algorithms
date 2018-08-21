class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        common = set(nums1)&set(nums2)
        res = []
        for n in common:
            res+=[n]*min(n1[n],n2[n])
        return res