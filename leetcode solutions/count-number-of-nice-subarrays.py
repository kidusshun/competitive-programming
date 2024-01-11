class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = []
        for i,num in enumerate(nums):
            if num%2!=0:
                odds.append(i)
        if len(odds) ==0:
            return 0
        l,r = 0,k-1
        ans = 0
        while r<len(odds):
            if l == 0:
                left = odds[l]+1
            else:
                left = odds[l]-odds[l-1]
            if r==len(odds)-1:
                right = len(nums) - odds[r]
            else:
                right = odds[r+1] - odds[r]
            ans+=right*left
            r+=1
            l+=1
        return ans