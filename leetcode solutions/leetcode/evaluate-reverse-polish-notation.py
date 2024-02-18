class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        string_stack=[]
        for char in tokens:
            if char == "*":
                num1=string_stack.pop()
                num2=string_stack.pop()
                result=num1*num2
                string_stack.append(result)
            elif char == "+":
                num1=string_stack.pop()
                num2=string_stack.pop()
                result=num1+num2
                string_stack.append(result)
            elif char == "-":
                num1=string_stack.pop()
                num2=string_stack.pop()
                result=num2-num1
                string_stack.append(result)
            elif char == "/":
                num1=string_stack.pop()
                num2=string_stack.pop()
                result=int(num2/num1)
                string_stack.append(result)
            else:
                string_stack.append(int(char))
        return string_stack.pop()
