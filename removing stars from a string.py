class Solution:
    def removeStars(self, s: str) -> str:
        s= list(s)
        ans=[]
        j=0
        while j< len(s):
            if s[j] == '*':
                ans.pop()
            else:
                ans.append(s[j])
            j+=1
        return ''.join(ans)