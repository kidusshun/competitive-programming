class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        for char in lst:
            if char ==".." and len(stack)>0:
                stack.pop()
            elif char =="" or char=="." or (char==".." and len(stack) ==0):
                continue
            else:
                stack.append(char)
        print(stack)
        return "/"+"/".join(stack)