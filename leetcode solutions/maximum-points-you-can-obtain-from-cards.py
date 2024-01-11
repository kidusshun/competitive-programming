class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0, len(cardPoints) - k
        sum_ = sum(cardPoints[r:])
        ans = sum_
        while r<len(cardPoints):
            sum_ += (cardPoints[l]-cardPoints[r])
            ans = max(sum_, ans)
            l+=1
            r+=1
        return ans 