class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        length= len(nums)
        left = 0
        right = sum(nums)
        answer = [0] * length

        for i in range(length):
            right -= nums[i]
            answer[i] = abs(right - left)
            left += nums[i]
        return answer