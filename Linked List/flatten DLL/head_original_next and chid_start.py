"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        Ohead =head
        if not head:
            return None
        
        head_original =None
        child_start =None
        
        while head:
            if head.child:
                child_start=child_end=head.child
                head.child =None
                child_start.prev =head
                if head.next:
                    head_original = head.next
                    while child_end.next:
                        child_end = child_end.next
                    child_end.next = head_original
                    if head_original.prev: 	#check if not None
                        head_original.prev = child_end
                head.next =child_start
            head = head.next
        return Ohead