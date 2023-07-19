class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        ans = float('inf')
        dist = [0] * k
        summ = sum(cookies)
        length = len(dist)
        return self.calculate(ans,0,dist, length, cookies, summ)
    def calculate(self,ans,k,dist, length,cookies,summ):
            for j in range(k, len(cookies)):
                i = 0
                while i< length:
                    new_dist = dist.copy()
                    new_dist[i] += cookies[j]
                    ans = self.calculate(ans,j+1,new_dist, length, cookies,summ)
                    i+=1
            if sum(dist) == summ:ans = min(max(dist), ans)
            return ans
