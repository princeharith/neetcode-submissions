# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        curr = dummy = ListNode(None)
        
        while l1 or l2:
            first_val, second_val = 0,0
            if l1:
                first_val = l1.val
            if l2:
                second_val = l2.val

            curr_val = first_val + second_val + carry
            carry = curr_val // 10
            value = curr_val % 10

            curr.next = ListNode(value)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        

        
        if carry:
            curr.next = ListNode(carry)

        
        # while dummy:
        #     print(dummy.val)
        #     dummy = dummy.next
        
        return dummy.next

