# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

        [1] -> [2] -> [3] <- [4]
        t
                                f
                    s
                    h2
                            p
                        <-      c
        h1                    h2
               h1n    h2n
               h1     h2
    d ->
    t   
               h2n    h1n    

    0->1->4->3->2
          d
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        tracker = head
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head1 = tracker
        head2 = prev

        dummy = ListNode()
        tracker = dummy

        while head2:
            head1n = head1.next
            head2n = head2.next

            dummy.next = head1
            dummy.next.next = head2
            
            dummy = dummy.next.next

            head1 = head1n
            head2 = head2n

        dummy.next = None

        return None


"""
    h 1 2 3 4
            f
        s
        h
            p
        <  c
        <      n
    1   2
d>       >


"""
