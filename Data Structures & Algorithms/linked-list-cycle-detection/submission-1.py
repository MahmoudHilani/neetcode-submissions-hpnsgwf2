# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow = head
        else:
            return False
        if head.next:
            fast = head.next
        else:
            return False
        while slow:
            if slow == fast:
                return True
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False