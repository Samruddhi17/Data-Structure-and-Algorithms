# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def seri_bst(root,res):
            if not root:
                return None
            seri_bst(root.left,res)
            res.append(root.val)
            seri_bst(root.right,res)
            return res     
        
        seri =[]
        seri =seri_bst(root,seri)
        if not seri or len(seri) ==1:
            return True
        for i in range(0,len(seri)-1):
            if seri[i] >= seri[i+1]:
                return False
        return True
       