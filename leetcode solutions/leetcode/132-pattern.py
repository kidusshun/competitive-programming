class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_ = nums[0]
        for num in nums:
            while stack and num > stack[-1][0]:
                stack.pop()
            # print(stack,num)
            if stack and stack[-1][1]<num<stack[-1][0]:
                return True
            stack.append((num, min_))
            min_ = min(min_, num)

        return False