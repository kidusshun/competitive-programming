class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i,j = 0, len(ans)-1

        for num in nums:
            if num%2 == 0:
                ans[i]=num
                i+=1
            else:
                ans[j]=num
                j-=1
        return ans