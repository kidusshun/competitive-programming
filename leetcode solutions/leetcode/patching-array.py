class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 1
        pref = 0
        j = 0
        patches = 0
        while pref < n:
            if j < len(nums) and nums[j] <= curr:
                pref+=nums[j]
                j+=1
            else:
                patches +=1
                pref +=curr
            curr = pref + 1
        return patches