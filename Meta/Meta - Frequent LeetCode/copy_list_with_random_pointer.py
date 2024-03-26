"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodesDict = {}
        
        current = head
        count = 0
        
        newNodeHead = Node(head.val)
        
        while current is not None:
            newNode = newNodeHead
            newNode.val = current.val
            
            if newNode.val in nodesDict:
                nodesDict[newNode.val]
            else:
                nodesDict[newNode.val] = newNode
            
            if current.random and current.random.val in nodesDict:
                newNode.random = nodesDict[current.random.val]
            elif current.random:
                nodesDict[current.random.val] = Node(current.random.val)
                newNode.random = nodesDict[current.random.val]
                
                
            if current.next and current.next.val in nodesDict:
                newNode.next = nodesDict[current.next.val]
            elif current.next:
                nodesDict[current.next.val] = Node(current.next.val)
                newNode.next = nodesDict[current.next.val]

            if count == 0:
                newNodeHead = newNode
                count += 1
            current = current.next
            