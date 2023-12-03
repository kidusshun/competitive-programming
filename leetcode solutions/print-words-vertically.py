class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_length = 0
        lst = s.split(" ")
        for word in lst:
            max_length = max(max_length,len(word))
        ans = []
        for i in range(max_length):
            curr = ""
            for word in lst:
                if i<len(word):
                    curr+=word[i]
                else:
                    curr+=" "
            ans.append(curr.rstrip())
        return ans