def reverseParentheses(s):
    stack=[]
    stack.reverse()
    for string in s:
        if string==")":
            str1=""
            while stack[len(stack)-1]!="(":
                string1=stack.pop()
                str1+=string1[::-1]
            stack.pop()
            stack.append(str1)
        else:
            stack.append(string)
    return "".join(stack)