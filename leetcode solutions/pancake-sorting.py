class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if sorted(arr) == arr:
            return []
        ans = []
        end = len(arr)
        i = 0
        while end > 1:
            max_ind = arr.index(end)
            if max_ind == end -1:
                end -=1
                continue
            if max_ind != 0:
                arr[:max_ind+1] = reversed(arr[:max_ind+1])
                ans.append(max_ind+1)
            arr[:end] = reversed(arr[:end])
            ans.append(end)
            end -= 1
        return ans