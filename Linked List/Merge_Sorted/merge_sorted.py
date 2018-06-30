# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        new_head = ret_head= ListNode(0)
        while l1 and l2:
            if l2.val < l1.val:
                new_head.next, l2 = l2, l2.next
            else:
                new_head.next,l1 = l1,l1.next
            new_head = new_head.next
        
        new_head.next = l1 or l2
        return ret_head.next