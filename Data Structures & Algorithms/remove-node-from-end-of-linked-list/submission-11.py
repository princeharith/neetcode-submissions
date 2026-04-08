# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #slow and fast pointer
        #move fast pointer to nth+1 node from slow
            #this will allow us to do slow.next = slow.next.next
            #we may need the prev actually in order to rewire the connection?

        dummy = ListNode(None)
        dummy.next = head
        
        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next

        