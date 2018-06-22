class Solution:
    def removeDuplicates(self, nums):
        if not nums:	#empty array
            return 0
        else:
            start = nums[0]		#unique element assigned
            j =1
            for i in nums[j:]:	#search until new element not found
                if start == i:	#if duplicate remove element
                    nums.remove(i)
                else:
                    start = i #change to new unique element
                    j = i+1	  #start scanning the array from next position to new unique element
            print (nums) 