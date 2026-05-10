# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        #      p2
        # 5 -> None
        # p1
    #prev
           
        
        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next
        
        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        
        prev.next = p1.next

        return dummy.next

        #prev to keep track of before target
        
        

