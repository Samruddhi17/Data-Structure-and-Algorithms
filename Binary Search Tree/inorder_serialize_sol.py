class Solution(object):
    def isValidBST(self, root):
        serialized = []
        self.inorder(root, serialized)
        for i in range(1, len(serialized)):
            if serialized[i-1] >= serialized[i]:
                return False
        return True

    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)