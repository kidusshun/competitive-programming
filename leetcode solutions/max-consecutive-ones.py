class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        counter = 0
        for num in nums:
            if num == 1:
                counter +=1
            else:
                ans.append(counter)
                counter = 0
        ans.append(counter)
        return max(ans)