class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        if not root or root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        if left:
            print("left",left.val)
        right = self.lowestCommonAncestor(root.right,p,q)
        if right:
            print("right",right.val)
        
        return root if left and right else left or right