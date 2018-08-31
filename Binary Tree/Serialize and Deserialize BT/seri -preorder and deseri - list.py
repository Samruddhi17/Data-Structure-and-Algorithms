# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.string =''
        self.preorder(root)
        return self.string
        
    def preorder(self,root):
        if root is None:
            self.string +='null '
            return 
        
        self.string += str(root.val) + ' '
        self.preorder(root.left) 
        self.preorder(root.right) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(' ')
  
        return self.makeTree(arr[:-1])
         
        
    def makeTree(self,arr):
        if not arr:
            return None
        val = arr.pop(0)
   
        if val =='null':
            return None
        root = TreeNode(val)

        root.left = self.makeTree(arr)
        root.right = self.makeTree(arr)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))