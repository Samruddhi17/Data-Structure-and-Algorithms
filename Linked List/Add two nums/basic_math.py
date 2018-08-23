# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=l3 = ListNode(0)
        carry =0
        while l1 or l2 or carry:
            if l1:
                x = l1.val
            else:
                x=0
            if l2:
                y = l2.val
            else:
                y=0    
            
            s = carry + x + y 
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            l3.next =ListNode(s)
            l1 =l1 and l1.next
            l2 = l2 and l2.next
            l3 = l3.next
        return res.next    