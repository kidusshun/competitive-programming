from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_deque = deque()
        d_deque = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R': r_deque.append(i)
            if senate[i] == 'D': d_deque.append(i)
        
        while r_deque and d_deque:
            r = r_deque.popleft()
            d = d_deque.popleft()

            if r < d: r_deque.append(n+r)
            else: d_deque.append(n+d)
        
        return 'Radiant' if r_deque else 'Dire'