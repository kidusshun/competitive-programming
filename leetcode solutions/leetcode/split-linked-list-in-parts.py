# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
        one_extra = length%k
        part_length = length//k
        ans = []
        while dummy.next:
            new_head = dummy
            new_curr = new_head
            counter = part_length
            while new_curr and counter >0:
                new_curr = new_curr.next
                counter -=1
            if one_extra>0:
                new_curr = new_curr.next
                one_extra -=1
            curr = dummy.next
            if new_curr:
                dummy.next = new_curr.next
                new_curr.next = None
            else:
                curr = new_curr
            ans.append(curr)
        while len(ans) < k:
            ans.append(None)
        return ans
        