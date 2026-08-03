# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        if not head or not head.next:
            return False

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: 
                break

        return fast == slow
