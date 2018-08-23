# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
       
        #reverse second half
        prev = None
        curr =slow
        temp = None
        
        while curr:
            temp =curr.next
            curr.next = prev
            prev =curr
            curr =temp
        
        while prev:
            if prev.val == head.val:
                prev= prev.next
                head = head.next
            else:
                return False
        return True    
        
    