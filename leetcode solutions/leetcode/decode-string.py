class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        curr = ""
        stack = []
        i = len(s)-1
        num = ""
        while i >=0:
            if s[i] == "[":
                while stack[-1]!="]":
                    curr += stack.pop()
                stack.pop()
                i-=1
                while i>=0 and s[i].isdigit():
                    num = s[i]+num
                    i-=1
                curr *= int(num)
                if len(stack) == 0:
                    ans = curr +ans
                else:
                    stack.append(curr)
                curr = ""
                num = ""
                i+=1
            elif s[i] != "]" and not stack:
                ans =s[i]+ans
            else:
                stack.append(s[i])
            i-=1
        print(ans)
        return ans