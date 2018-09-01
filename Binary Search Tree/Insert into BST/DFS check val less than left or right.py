# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.checkdepth(root,val)
        return root
        
    def checkdepth(self,root,val):
            
        if not root:
            return TreeNode(val)
        else:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return
                else:
                    self.checkdepth(root.left,val)
            if root.val<val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return
                else:
                    self.checkdepth(root.right,val)
        return