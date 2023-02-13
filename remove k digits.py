class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for number in num:
            while k>0 and len(stack)>0 and stack[-1]>number:
                stack.pop()
                k-=1
            stack.append(number)
        while k>0:
            stack.pop()
            k-=1
        stack = "".join(stack).lstrip("0")
        if stack:
            return stack
        else:
            return "0"