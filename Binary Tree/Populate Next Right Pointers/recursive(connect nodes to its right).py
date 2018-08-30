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
        
        if root.left and root.right:
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left   # 2's left = 5 so 5's next will be 2's next left ie 3's left = 6. 5->6
        self.connect(root.left)
        self.connect(root.right)