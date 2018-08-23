# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head,prev =None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return prev
        else:
            temp =head.next 
            head.next = prev
        return self.reverseList(temp, head) #new_head and prev= head