class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        base = nums[-1]
        ops = 0
        for i in range(len(nums)-2,-1,-1):
            compar = nums[i]
            if compar <= base:
                base = compar
                continue
            else:
               rows = math.ceil(compar/base)
               ops+=rows-1
               base = compar//rows
        return ops