# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst=[]
        max_sum=float('-inf')
        current=head
        while current:
            lst.append(current.val)
            current=current.next
        i,j=0,len(lst)-1
        while i<len(lst)//2:
            val=lst[i]+lst[j]
            max_sum=max(max_sum,val)
            i+=1
            j-=1
        return max_sum


