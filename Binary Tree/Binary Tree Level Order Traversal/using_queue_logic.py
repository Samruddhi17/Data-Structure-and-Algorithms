# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result =[]
        if root is None:
            return []
        
        current_level = [root]
        while current_level:
            result.append([curr.val for curr in current_level])
            current_level =[child for curr in current_level for child in (curr.left,curr.right) if child]
            
        return result        
            
            