# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        prev = ListNode(None)
        prev.next = head

        dummy = ListNode(0)
        dummy = prev

        for _ in range(n):
            if fast:
                fast = fast.next
        
        while True:
            if fast is None:
                prev.next = head.next
                break
            head = head.next
            prev = prev.next
            fast = fast.next
        
        return dummy.next