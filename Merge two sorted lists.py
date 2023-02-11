# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
           return list2
        elif list2 == None:
            return list1
        pointer1=ListNode()
        pointer2=pointer1
        while list1 and list2:
            if list1.val < list2.val:
                pointer2.next=list1
                list1=list1.next
            else:
                pointer2.next=list2
                list2=list2.next
            pointer2=pointer2.next
        if list1:
            pointer2.next=list1
        else:
            pointer2.next=list2
        return pointer1.next
