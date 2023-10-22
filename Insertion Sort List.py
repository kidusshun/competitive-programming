# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # [4,2,1,3]
    # [2,4,1,3]
    def insertionSortList(self, head):
        curr = head.next
        while curr:
            comp = head
            while comp and curr.val > comp.val:
                comp = comp.next
            comp.val, curr.val = curr.val, comp.val
            curr = curr.next
        return head

a = ListNode(
    val=4,
    next=ListNode(
        val=2,
        next=ListNode(
            val=1,
            next=ListNode(
                val=3,
                next=None
            )
        )
    )
)

s = Solution()

s.insertionSortList(a)