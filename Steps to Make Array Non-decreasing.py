class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = [[nums[0], 0]]
        ans = 0
        
        for num in nums[1:]:
            t = 0
            while stack and stack[-1][0] <= num:
                t = max(t, stack[-1][1])
                stack.pop()
            if stack: 
                t += 1
            else:
                t = 0
            ans = max(ans, t)
            stack.append([num, t])
            
        return ans