class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        
        i,j = 0,0

        while i < len(s):
            if s[i]!='#':
                ans1.append(s[i])
            elif s[i]=='#' and len(ans1)!=0:
                ans1.pop()
            i+=1
        
        while j < len(t):
            if t[j]!='#':
                ans2.append(t[j])
            elif t[j]=='#' and len(ans2)!=0:
                ans2.pop()
            j+=1
        return ans1 == ans2