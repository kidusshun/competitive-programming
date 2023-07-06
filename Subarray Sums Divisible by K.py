class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        i=0
        sub_sum=0
        ans=0
        for j in range(len(nums)):
            sub_sum += nums[j]
            while i <= j:
                if sub_sum%k == 0:
                    ans +=1
                sub_sum -=nums[i]
                i+=1
        
        return ans

s = Solution()
s.subarraysDivByK([4,5,0,-2,-3,1], 5)