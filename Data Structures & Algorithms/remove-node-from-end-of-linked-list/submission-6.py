# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0

        first_pass, second_pass = head, head
        while first_pass:
            list_length += 1
            first_pass = first_pass.next
        

        if list_length == 1:
            return None
    
        
        
        nodeToDelete = list_length-n
        if nodeToDelete == 0:
            head = head.next
            return head
            
        while second_pass:
            nodeToDelete -= 1
            if nodeToDelete == 0:
                    second_pass.next = second_pass.next.next
            second_pass = second_pass.next
        return head
        
        
        