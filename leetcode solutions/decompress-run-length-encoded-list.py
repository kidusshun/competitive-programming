class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while 2*i +1<len(nums):
            freq = nums[2*i]
            val = nums[2*i+1]
            ans.extend([val]*freq)
            i+=1
        return ans