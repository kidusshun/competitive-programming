class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(sub, k):
            ans.append(sub.copy())
            if len(ans) == 2**length:
                return  
            while k < length:
                sub.append(nums[k])
                subs(sub, k+1)
                sub.pop()
                k+=1
        length = len(nums)
        ans = []
        subs([], 0)
        return ans