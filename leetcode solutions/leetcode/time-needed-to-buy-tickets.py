class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        time = 0
        while queue:
            curr = queue.popleft()
            time +=1
            if k == 0:
                if curr == 1:
                    return time
                else:
                    queue.append(curr-1)
                    k=len(queue)
            elif curr >1:
                queue.append(curr-1)
            k-=1
        return time