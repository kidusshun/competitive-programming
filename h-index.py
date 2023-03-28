class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse=True)
        counter=0
        for i,j in enumerate(citations):
            if i<j:
                counter +=1
            else:
                break
        return counter