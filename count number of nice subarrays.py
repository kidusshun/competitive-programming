class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        num_odds,num_sub = 0,0
        dic[0] = 1
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                num_odds+=1
            num_sub += dic[num_odds-k]
            dic[num_odds]+=1
        return num_sub
            