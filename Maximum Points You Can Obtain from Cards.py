class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ind1,ind2=0, len(cardPoints)-k
        total=sum(cardPoints[ind2:])
        result=total
        while ind2<len(cardPoints):
            total=total +cardPoints[ind1]-cardPoints[ind2]
            if result<total:
                result=total
            ind2+=1
            ind1+=1
        return result
            