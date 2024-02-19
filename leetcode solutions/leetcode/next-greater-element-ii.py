class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        for i in range(2*len(nums)):
            while stack and stack[-1][0]<nums[i%len(nums)]:
                popped = stack.pop()
                if ans[popped[1]] == -1:
                    ans[popped[1]] = nums[i%len(nums)]
            stack.append((nums[i%len(nums)],i%len(nums)))
        return ans