# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        tracker = head
              
        while head:
            length += 1
            head = head.next

        dummy = ListNode()
        dummy.next = tracker

        head = tracker
        prev= dummy
        count = 0

        while count != length - n:
            count += 1
            prev = head
            head = head.next

        prev.next = head.next

        return dummy.next
