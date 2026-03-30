# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for i in range(length // 2):
            curr = curr.next
        tmp = curr.next
        curr.next = None
        revPtr = tmp
        prev = None
        while revPtr:
            tmp2 = revPtr.next
            revPtr.next = prev
            prev = revPtr
            revPtr = tmp2
        curr = head
        while curr and prev:
            tmp3 = curr.next
            tmp4 = prev.next
            curr.next = prev
            prev.next = tmp3
            prev = tmp4
            curr = tmp3