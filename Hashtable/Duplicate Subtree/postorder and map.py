class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        
        self.res =[]
        self.hashmap ={}
        self.preorder(root)
        return self.res
        
    def preorder(self,root):
        if not root:
            return '#'
        
        tree =self.preorder(root.left)+self.preorder(root.right)+str([root.val])
        
        if tree in self.hashmap and self.hashmap[tree]==1:
            self.res.append(root)
        self.hashmap[tree]=self.hashmap.get(tree,0)+1
        return tree