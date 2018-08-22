# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        curr_level = [root]
        while curr_level:
            node =curr_level.pop()
            if node:
                node.left,node.right =node.right,node.left
                curr_level+= node.left,node.right
        return root