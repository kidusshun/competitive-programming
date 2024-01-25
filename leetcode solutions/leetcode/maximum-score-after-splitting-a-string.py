class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(num) for num in s]

        count = sum(nums)
        zeros = []
        num_zeros = 0
        ones = []
        max_ = 0

        for i in range(len(nums)-1):
            if nums[i] == 1:
                count-=1
            else:
                num_zeros+=1
            curr = count+num_zeros  
            if curr > max_:
                max_ = curr

        return max_