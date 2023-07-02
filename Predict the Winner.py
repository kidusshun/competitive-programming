class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo ={}

        def score(left,right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[i,j]

            score_left = nums[left] - score(left + 1, right)
            score_right = nums[right] - score(left, right - 1)

            return max(score_left, score_right)
        
        return score(0,len(nums)-1) >= 0