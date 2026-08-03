# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        if not head.next:
            return head

        prev = head
        curr = head.next
        prev.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
"""
 
 h > 1 > 2 > 3

 p < c   n
     p < c   n
         p < c  None
             p   c
"""