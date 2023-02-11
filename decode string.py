class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char =="]":
                string=""
                while stack[0]!="[":
                    string=stack.pop(0) + string
                stack.pop(0)
                num=""
                while stack and stack[0].isdigit():
                    num=stack.pop(0)+num
                stack.insert(0,int(num)*string)
            else:
                stack.insert(0,char)
        stack.reverse()
        return "".join(stack)
            