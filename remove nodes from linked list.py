# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
     def removeNodes(self, head):
        if not head: return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head

lst=[5,2,13,3,8]
head=ListNode(lst[0])
current=head
for num in lst[1:]:
        new_node = ListNode(num)
        current.next = new_node
        current = current.next
s=Solution()
s.removeNodes(head)