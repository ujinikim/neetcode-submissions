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
        deepCopyDict = {None: None}

        tempHead = head
        while tempHead:
            deepCopyDict[tempHead] = Node(tempHead.val)
            tempHead = tempHead.next

        tempHead = head
        while tempHead:
            deepCopyDict[tempHead].next = deepCopyDict[tempHead.next]
            deepCopyDict[tempHead].random = deepCopyDict[tempHead.random]
            tempHead = tempHead.next

        return deepCopyDict[head]
            
