# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        # Recursion
        new_head = self.reverseList(head.next)

        #Make the next head to point to itself
        head.next.next = head

        #Remove the original
        head.next = None

        #Return the new_head
        return new_head