# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        self.arr = []
        self.seri(root)
        if k <=len(self.arr):
            return self.arr[k-1]
        else:
            return -1
            
    
    def seri(self,root):
        if not root:
            return None
        else:
            self.seri(root.left)
            self.arr.append(root.val)
            self.seri(root.right)

        