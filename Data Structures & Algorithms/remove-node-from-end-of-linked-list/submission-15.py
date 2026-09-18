# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                
        # dummy -> 1 -> 2 -> 4 -> None
        #              prev
        #                    p1
        #                              p2


        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next
        
        dummy = ListNode(None)
        dummy.next = head
        last_node = dummy
        while p2:
            last_node = p1
            p1 = p1.next
            p2 = p2.next

        last_node.next = p1.next

        return dummy.next
