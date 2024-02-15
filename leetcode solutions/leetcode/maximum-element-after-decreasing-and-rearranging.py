class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_ = len(arr)
        surplus = 0
        for key in count:
            if key > max_:
                surplus +=count[key]
        for i in range(len(arr),0,-1):
            if i in count:
                val = count[i]
                surplus += val-1
            elif i not in count:
                if surplus>0:
                    surplus -=1
                else:
                    max_ -=1
        return max_