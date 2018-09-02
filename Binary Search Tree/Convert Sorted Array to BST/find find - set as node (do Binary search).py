# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        """
        
        Since the array in sorted. mid is root.
        left half of array = left subtree
        right hasf = right subtree
        
        """
        self.nums = nums
        return self.BST(0,len(nums)-1)
    
    def BST(self,l,r):
        if l>r:
            return None
        mid = (l+r)//2
        
        root = TreeNode(self.nums[mid])
        root.left = self.BST(l,mid-1)
        root.right = self.BST(mid+1,r)
        
        return root
        