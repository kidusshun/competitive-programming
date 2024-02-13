class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if rem== 0:
            return 0
        d = {0:-1}
        pref = 0
        min_length = len(nums)
        for i, num in enumerate(nums):
            pref += num
            print(pref)
            if (pref- rem)%p in d:
                min_length = min(min_length, i - d[(pref- rem)%p])
            d[pref%p] = i
        if min_length == len(nums): return -1
        return min_length