class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        summ_ = sum(nums)
        absolute = []
        length = len(nums)
        pref = [0]
        for num in nums:
            pref.append(num+pref[-1])
        for i in range(len(nums)):
            val = (nums[i]*i - pref[i]) + (pref[-1] - pref[i+1]) - nums[i]*(length-1-i)
            absolute.append(val)
        return absolute