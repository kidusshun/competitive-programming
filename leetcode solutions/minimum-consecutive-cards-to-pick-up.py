class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float("inf")
        l,r = 0,0
        seen = set()
        while r< len(cards):
            if cards[r] not in seen:
                seen.add(cards[r])
            else:
                while cards[r] in seen:
                    seen.discard(cards[l])
                    l+=1
                ans = min(ans, r-l+2)
                seen.add(cards[r])
            r+=1
        if ans == float("inf"):
            return -1
        return ans