# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        seen = set()
        while curr:
            if curr not in seen:
                seen.add(curr)
            else:
                return curr
            curr = curr.next
        return None