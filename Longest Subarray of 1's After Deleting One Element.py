class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        count = {}
        i,j = 0, 0
        length = len(nums)
        ans = 0

        while j< length:
            count[nums[j]] = count.get(nums[j],0) + 1

            while 0 in count and count[0]>1:
                if nums[i] == 0:
                    count[0] -= 1
                i+=1
            ans = max(j-i,ans)
            j+=1
        return ans
s = Solution()
s.longestSubarray([1,0,0,0,0])