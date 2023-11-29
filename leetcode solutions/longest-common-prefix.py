class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        min_length = float("inf")
        for st in strs:
            min_length = min(min_length, len(st))
        if min_length == 0:
            return ""
        i = 0
        while i < min_length:
            curr = strs[0][i]
            for st in strs[1:]:
                if st[i] !=curr:
                    return st[:i]
            i+=1
        else:
            print(i)
            return strs[0][:i]