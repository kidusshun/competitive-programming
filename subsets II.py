class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subs(sub, k):
            count = dict(Counter(sub))
            if sub not in ans and count not in diction:
                ans.append(sub.copy())
                diction.append(count)
            if len(ans) == 2**length:
                return  
            while k < length:
                sub.append(nums[k])
                subs(sub, k+1)
                sub.pop()
                k+=1
        length = len(nums)
        ans = []
        diction = []
        subs([], 0)
        ans.sort()
        return ans