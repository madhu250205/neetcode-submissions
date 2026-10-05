# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 1: Advance right pointer by n steps to create the gap
        for _ in range(n):
            right = right.next

        # Step 2: Advance both pointers until right hits the end
        while right:
            left = left.next
            right = right.next

        # Step 3: Delete the nth node from the end
        left.next = left.next.next

        return dummy.next