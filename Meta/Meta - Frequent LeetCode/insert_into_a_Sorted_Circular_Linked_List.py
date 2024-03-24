"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        insertValNode = Node(insertVal,None)
        if head is None:
            insertValNode.next = insertValNode
            return insertValNode

        if head.next is head:
            insertValNode.next = head
            head.next = insertValNode
            return head
        
        current = head
        while True:
            if current.val == current.next.val:
                current = current.next
            if (current.val <= insertVal and insertVal <= current.next.val and current.val <= current.next.val) or \
                (current.val >= insertVal and current.next.val >= insertVal and current.next.val <= current.val) or \
                (current.val <= insertVal and current.next.val <= current.val and current.next.val <= insertVal):
                temp = current.next
                insertValNode.next = temp
                current.next = insertValNode
                break
            current = current.next
        return head