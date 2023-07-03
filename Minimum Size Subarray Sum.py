class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i,j=0,1
        new_num = nums[i:j]
        size=float('inf')
        while j <= len(nums):
            if sum(new_num) >= target and len(new_num)<size:
                size=len(new_num)
                while i < j:
                    new_num = nums[i:j]
                    if sum(new_num) >= target and len(new_num)<size:
                        size=len(new_num)
                    i+=1
        
            j+=1
            new_num = new_num + nums[j]
        if size == float('inf'): return 0
        return size


s = Solution()
s.minSubArrayLen(11, [10,5,13,4,8,4,5,11,14,9,16,10,20,8])