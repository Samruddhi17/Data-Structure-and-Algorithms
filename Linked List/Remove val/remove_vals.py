# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1) #start from Null
        dummy_head.next = head
       
        curr = dummy_head
        while curr.next !=None:
            if curr.next.val==val:
                curr.next = curr.next.next 
            else:
                curr = curr.next
        return dummy_head.next