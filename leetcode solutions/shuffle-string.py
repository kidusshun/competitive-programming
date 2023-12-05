class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""]* len(s)
        for i,char in enumerate(s):
            ind = indices[i]
            ans[ind] = char
        return "".join(ans)