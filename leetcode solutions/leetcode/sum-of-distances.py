class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def absDiff(lst):
            absolute = []
            length = len(lst)
            pref = [0]
            for num in lst:
                pref.append(num+pref[-1])
            for i in range(len(lst)):
                val = (lst[i]*i - pref[i]) + (pref[-1] - pref[i+1]) - lst[i]*(length-1-i)
                absolute.append(val)
            return absolute
        
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)
        for key in d.keys():
            lst = d[key]
            sth = absDiff(lst)
            lst = list(reversed(sth))
            d[key] = lst
        ans = nums.copy()
        
        for i,num in enumerate(nums):
            ans[i] = d[num][-1]
            d[num].pop()
        
        return ans
                

            