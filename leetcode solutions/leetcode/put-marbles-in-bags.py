class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cost = []
        for i in range(len(weights)-1):
            cost.append(weights[i]+weights[i+1])
        
        cost.sort()
        min_,max_ = 0,0
        i,j = 0,len(cost)-1
        
        while k>1:
            min_ += cost[i]
            max_ += cost[j]
            i+=1
            j-=1
            k-= 1
        return max_ - min_