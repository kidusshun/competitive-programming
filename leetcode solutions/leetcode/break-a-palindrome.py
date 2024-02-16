class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        ans = ""
        a_pos = -1
        for i, char in enumerate(palindrome):
            if char == "a":
                a_pos = i
                ans+=char
            else:
                if i==len(palindrome)//2 and len(palindrome)%2!=0:
                    ans+=char
                    continue
                ans+= "a"
                if i < len(palindrome)-1:
                    ans+=palindrome[i+1:]
                return ans
        print(ans)
        if ans == palindrome and a_pos==-1:
            return ""
        
        elif ans == palindrome and a_pos != -1:
            return palindrome[:a_pos] +"b"+palindrome[a_pos+1:]