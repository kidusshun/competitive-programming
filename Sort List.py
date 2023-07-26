# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        lst = []

        while curr:
            lst.append(curr.val)
            curr = curr.next
        lst.sort()

        root = ListNode(lst[0])
        prev = root
        for num in lst[1:]:
            curr = ListNode(num)
            prev.next = curr
            prev = curr
        return root