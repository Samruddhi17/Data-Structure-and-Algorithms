# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        
        count = 1 # count nodes in the list. 
        cur = head
        while cur.next:
            count += 1
            cur = cur.next
        cur.next = head # connect tail to head. Make the linked list as a 'ring'
        
        # We then want to locate the head and tail of our returned list. 
        # We can locate the new tail, which can be obtained by moving `count - k % count' steps. The new head will be tail.next given the ring structure.
        cur = head
        steps = count - k % count - 1
        for i in range(steps): 
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head
  