class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        length = len(nums)

        prefix = [0] * length

        prefix[0] = nums[0]

        for i in range(1,length):

            prefix[i] = prefix[i-1] + nums[i]

        return prefix