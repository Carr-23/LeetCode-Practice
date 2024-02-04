# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp.next is not None:
            temp = temp.next
            count += 1

        for i in range(-(count // -2)):
            head = head.next

        return head
