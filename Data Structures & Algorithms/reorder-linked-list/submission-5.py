# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(node):
            new_head = None
            while node:
                temp = node.next
                node.next = new_head

                new_head = node
                node = temp
            return new_head


        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = reverse_list(slow.next)
        slow.next = None

        first = head
        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1

            first, second = n1, n2
        

        

