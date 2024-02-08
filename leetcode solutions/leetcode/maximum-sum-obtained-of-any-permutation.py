class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0]*(len(nums)+1)
        for start,end in requests:
            pref[start] += 1
            pref[end+1] -= 1
        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        print(pref)
        pref.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)):
            res += nums[i]*pref[i]
        return res %(10**9 + 7)
