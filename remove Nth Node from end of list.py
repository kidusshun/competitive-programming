# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return head.next
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        pos=length-n
        length=0
        current=head
        if pos==0:
            head=head.next
            return head
        else:
            while current:
                length+=1
                if length == pos:
                    current.next= current.next.next
                current=current.next
            return head
