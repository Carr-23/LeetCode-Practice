# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newList = None

        if list1 is None:
            newList = list2
            return newList
        elif list2 is None:
            newList = list1
            return newList

        if list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            newList = list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            newList = list1

        return newList
