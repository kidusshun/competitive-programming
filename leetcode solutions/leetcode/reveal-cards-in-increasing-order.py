class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque(range(len(deck)))

        ans = [0]*len(deck)
        i = 0
        while q:
            left = q.popleft()
            ans[left] = deck[i]
            i+=1
            if q:
                q.append(q.popleft())
        return ans