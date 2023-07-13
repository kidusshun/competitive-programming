class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        length = len(nums)
        for i in range(length):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        ans = 0
        for i in range(length-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                j = stack.pop()
                ans = max(ans, i-j)
        return ans