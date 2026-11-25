# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #             c
        # -1 -> 5 -> None
        #       n
        #  p
           
            
        curr = head
        for _ in range(n):
            curr = curr.next
        
        sentinel = ListNode(-1)
        sentinel.next = head

        prev = sentinel
        node_to_remove = head
        while curr:
            curr = curr.next
            node_to_remove = node_to_remove.next
            prev = prev.next
        
        prev.next = node_to_remove.next
        return sentinel.next


        
        