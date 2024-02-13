# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        lengthA = 0
        while currA:
            lengthA+=1
            currA = currA.next
        lengthB = 0
        while currB:
            lengthB+=1
            currB = currB.next
        diff = abs(lengthA - lengthB)
        currA = headA
        currB = headB
        if lengthA > lengthB:
            while currA and diff>0:
                currA = currA.next 
                diff -=1
        else: 
            while currB and diff > 0:
                currB = currB.next
                diff -=1
        

        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None
