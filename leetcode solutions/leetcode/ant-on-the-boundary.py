class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for num in nums[1:]:
            pref.append(num+pref[-1])
        return pref.count(0)