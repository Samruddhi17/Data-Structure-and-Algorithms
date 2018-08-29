# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def checksym(sub_left,sub_right):
            
            if not sub_left and not sub_right:
                return True
            
            if not sub_left or not sub_right:
                return False
            
            if sub_left and sub_right: #vals , outer tree nodes and inner tree nodes
                return (sub_left.val ==sub_right.val and checksym(sub_left.left,sub_right.right) and checksym(sub_left.right,sub_right.left))   
            else:
                return False
        
        if not root:
            return True
        else:
            return checksym(root.left,root.right)
        