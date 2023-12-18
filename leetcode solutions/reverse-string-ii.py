class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        reverse = True
        if len(s)<k:
            return s[::-1]
        for i in range(k,len(s)+1,k):
            word = s[i-k:i]
            print(word)
            if reverse:
                ans+=word[::-1]
                reverse = False
            else:
                ans+=word
                reverse=True
        if len(s)%k!=0 and reverse:
            ans+=s[len(s)-(len(s)%k):][::-1]
        else:
            ans+=s[len(s)-(len(s)%k):]
        return ans