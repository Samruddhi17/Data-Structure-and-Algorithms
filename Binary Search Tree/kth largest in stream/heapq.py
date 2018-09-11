class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k =k
        self.nums =nums
        heapq.heapify(self.nums) #create min heapq
        
        while(len(self.nums))>self.k: #keep only k elements with k on top
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]: #replace top if new element is large
            heapq.heapreplace(self.nums,val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)