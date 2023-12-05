class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3,-1,-1):
            longest = nums[i+2]
            second_longest = nums[i+1]
            third_longest = nums[i]
            if second_longest + third_longest > longest:
                return third_longest + second_longest +longest
        return 0