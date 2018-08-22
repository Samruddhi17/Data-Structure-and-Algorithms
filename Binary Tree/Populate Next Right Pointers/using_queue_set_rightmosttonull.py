# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        
        curr_level = [root]
        right =None
        
        while curr_level:
            for curr in curr_level:
                curr.next =right
                right = curr
            right =None    
            curr_level = [child for curr in curr_level for child in (curr.right, curr.left) if child]
                         