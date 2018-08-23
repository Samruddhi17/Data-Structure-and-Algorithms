# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        if root:
            x =root.left 
            root.left = root.right
            root.right =x
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root