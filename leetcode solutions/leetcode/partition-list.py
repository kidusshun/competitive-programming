# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        pre,bigger = dummy,head
        while bigger and bigger.val <x:
            bigger = bigger.next
            pre = pre.next
        if not bigger:
            return head
        preSmall,smaller = bigger,bigger.next
        while smaller:
            if smaller.val < x:
                preSmall.next = smaller.next
                curr = smaller
                pre.next = curr
                curr.next = bigger
                pre = pre.next
                smaller = preSmall.next
            else:
                smaller = smaller.next
                preSmall = preSmall.next
        return dummy.next

        