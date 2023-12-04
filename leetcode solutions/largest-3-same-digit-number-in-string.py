class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = []
        for i in range(10):
            if f"{i}"*3 in num:
                nums.append(i)
        if len(nums) == 0:
            return ""
        return f"{max(nums)}"*3