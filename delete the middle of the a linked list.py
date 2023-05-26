# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        slow,fast=head,head
        nex=slow.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            prev=prev.next
            nex=nex.next
        prev.next=nex
        return dummy.next