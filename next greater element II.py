class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [-1]*length
        stack = []

        for i in range(2* length):
            num = nums[i%length]
            while stack and num > stack[-1][1]:
                j,value = stack.pop()
                ans[j] = num
            stack.append((i%length,num))
        return ans

s = Solution()
s.nextGreaterElements([1,2,3,4,3])