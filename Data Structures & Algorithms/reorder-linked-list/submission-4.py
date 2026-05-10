# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #getting the second half, cutting the list
        l2 = slow.next
        slow.next = None

        #l2 is the second half of the list
        new_head = None
        while l2:
            temp = l2.next
            l2.next = new_head

            new_head = l2
            l2 = temp
        
        #now new_head is our new_list
        prev = ListNode(0)
        prev.next = head
        while head and new_head:
            temp = head.next
            head.next = new_head
            
            temp2 = new_head.next
            new_head.next = temp
            
            head, new_head = temp, temp2



        