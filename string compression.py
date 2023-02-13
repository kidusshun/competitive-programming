class Solution:
    def compress(self, chars: List[str]) -> int:
        ind =0
        ans=0
        while ind < len(chars):
            length=1
            while ((ind+length)<len(chars)) and chars[ind + length] == chars[ind]:
                length+=1
            chars[ans]=chars[ind]
            ans+=1
            if length > 1:
                string=str(length)
                chars[ans:ans+len(string)] =list(string)
                ans += len(string)
            ind+=length
        return ans