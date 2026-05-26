"""
141. Linked List Cycle

fast-slow linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            nextFast = fast.next.next
            nextSlow = slow.next

            if nextFast == nextSlow:
                return True

            fast = nextFast
            slow = nextSlow
        
        return False
