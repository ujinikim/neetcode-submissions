# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head

        temp = res
        for i in range(n):
            temp = temp.next


        slow = res
        prev = None
        while temp:
            prev = slow
            slow = slow.next
            temp = temp.next

        prev.next = slow.next

        return res.next
