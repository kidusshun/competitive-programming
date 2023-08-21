# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val,i))
                lists[i] = lists[i].next

        ans = ListNode()    
        latest = ans
        while heap:
            val,i = heappop(heap)
            latest.next = ListNode(val)
            latest = latest.next
            if lists[i]:
                heappush(heap,(lists[i].val,i))
                lists[i] = lists[i].next
        return ans.next 