class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root