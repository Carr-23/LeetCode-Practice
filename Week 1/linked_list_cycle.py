# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        tort = head
        hare = tort.next
        while tort and hare:
            if hare.next is None:
                return False

            hare = hare.next.next
            tort = tort.next

            if hare == tort:
                return True
        return False
