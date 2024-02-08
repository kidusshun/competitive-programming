# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        pos = 1
        while curr and pos < left:
            curr = curr.next
            pos+=1
        lst = []
        l_node = curr
        while pos<=right:
            lst.append(curr.val)
            curr = curr.next
            pos+=1
        while len(lst) > 0:
            l_node.val = lst[-1]
            lst.pop()
            l_node = l_node.next
        return head