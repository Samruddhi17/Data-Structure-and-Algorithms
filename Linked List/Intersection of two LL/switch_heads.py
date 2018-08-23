# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB,count=0):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        if headA is None or headB is None:
            return None
       
        A = headA
        B = headB
        while A is not B:
            if not A:
                A = headB
            else:
                A=A.next
            if not B:
                B=headA
            else:
                B=B.next
        return A        