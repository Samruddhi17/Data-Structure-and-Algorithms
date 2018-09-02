# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        Use the trick to indicate whether the height is greater than 1. Here, as long as the height is greater than 1, the return value of each layer is set to -1. If the value returned to root is not -1, the height is less than 1, but return A -1 proves that the tree is unbalanced at a certain level.
        """
        return self.dfs(root)!=-1
    
    def dfs(self,root):
        if not root:
            return 0
        dep_left =self.dfs(root.left)
        dep_right = self.dfs(root.right)
        print(root.val,dep_left)
        print(root.val,dep_right)
        
        if abs(dep_left -dep_right) >1 or dep_left==-1 or dep_right ==-1:
            return -1
        
        return max(dep_left,dep_right)+1
        
        
        