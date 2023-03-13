class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i, num in enumerate(nums):
            nums[i]=int(num)
        nums.sort()
        nums.reverse()
        return str(nums[k-1])