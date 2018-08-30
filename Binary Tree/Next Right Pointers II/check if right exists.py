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
        
        first = root
        while first:
            node = first
            first_next = None
            prev= None
            
            while node:
                if node.left:
                    if not first_next:
                        first_next = node.left
                        prev = node.left
                    else:
                        prev.next = node.left
                        prev = node.left
                if node.right:
                    if not first_next:
                        first_next = node.right
                        prev = node.right
                    else:
                        prev.next = node.right
                        prev =node.right
                node = node.next
            first = first_next