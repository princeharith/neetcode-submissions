# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        #now we have the left
        curr = prev.next

        #we can start reversing from here, keep a reference to original left
        original_left = curr
        prev_node = None

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev_node

            prev_node = curr
            curr = temp
        
        prev.next = prev_node
        original_left.next = curr

        return dummy.next

