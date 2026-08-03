# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)

        tracker = [True] * k
        done = [False] * k

        dummy = ListNode()
        head = dummy
        
        while tuple(tracker) != tuple(done):
            
            tmp = ListNode()
            tmp.val=1001
            lowest = (-1,tmp)

            for index, track in enumerate(lists):
                
                if not tracker[index]:
                    continue

                if not track: 
                    tracker[index] = False
                    continue

                if track.val <= lowest[1].val:
                    lowest = (index, track)

            if lowest[1] == tmp:
                dummy.next = None
            else:
                dummy.next = lowest[1]
                dummy = dummy.next

                node = lowest[1]
                node = node.next
                lists[lowest[0]] = node

        return head.next
