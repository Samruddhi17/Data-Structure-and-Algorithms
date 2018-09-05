class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.original = list(nums) #new list to avoid changes
       

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        nums = self.original
        self.original = list(self.original)
        return nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.arr)):
            r = random.randrange(i,len(self.arr))  #do not shuffle prev ones
            self.arr[i],self.arr[r] = self.arr[r],self.arr[i] 
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()