class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = defaultdict(int)
        curr = 0
        for num in nums:
            curr += num
            pref[curr%k] +=1
        ans = 0
        for rem in pref:
            ans += pref[rem] *(pref[rem]-1)//2
        return ans + pref[0]