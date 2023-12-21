class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = sum(nums)
        zeros = []
        num_zeros = 0
        ones = []
        max_ = max(count,len(nums)-count)
        ans =[] 
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(count)
                zeros.append(num_zeros)
                count-=1
            else:
                ones.append(count)
                zeros.append(num_zeros)
                num_zeros+=1
            curr = zeros[-1]+ones[-1]    
            if curr > max_:
                max_ = curr
                ans = [i]
            elif curr == max_:
                ans.append(i)
        if num_zeros+count> max_:
            ans = len(nums)
        elif num_zeros+count == max_:
            ans.append(len(nums))
        return ans