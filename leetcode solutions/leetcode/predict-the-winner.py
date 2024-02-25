class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def score(l,r):
            if l > r:
                return 0

            left = nums[l] - score(l+1,r)
            right = nums[r] - score(l, r-1)

            return max(left,right)
        val = score(0,len(nums)-1)
        if val>=0:
            return True
        return False