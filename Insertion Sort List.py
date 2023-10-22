# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # [4,2,1,3]
    # [2,4,1,3]
    # [1,2,4,3]
    # [1,2,3,4]
    def insertionSortList(self, head):
        dummy = ListNode(0,head)
        prev,curr =head, head.next

        while curr:
            if curr.val >=prev.val:
                prev, curr = curr, curr.next
                continue
            
            temp = dummy
            while curr.val < temp.next.val:
                temp = temp.next
            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next
        return dummy.next

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