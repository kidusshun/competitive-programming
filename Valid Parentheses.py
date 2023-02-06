class Solution:
    def isValid(self, s: str) -> bool:
        stack_1=[]
        stack_2=[]
        for char in s:
            if char == '(' or char == '[' or char =='{':
                stack_1.append(char)
            else:
                stack_2.append(char)
                if char == ')' and len(stack_1)!=0 and stack_1[len(stack_1)-1]=='(':
                    stack_1.pop()
                    stack_2.pop()
                elif char == ']' and len(stack_1)!=0 and stack_1[len(stack_1)-1]=='[':
                    stack_1.pop()
                    stack_2.pop()
                elif char == '}' and len(stack_1)!=0 and stack_1[len(stack_1)-1]=='{':
                    stack_1.pop()
                    stack_2.pop()
                elif len(stack_1)==0:
                    return False
        if len(stack_1)==0 and len(stack_2)==0:
            return True
        else:
            return False
                