class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0"
        ans = [0] * (len(num2) + len(num1))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                ans[i1+i2] += digit
                ans[i1+i2+1] += (ans[i1+i2]//10)
                ans[i1+i2] = ans[i1+i2]%10
        
        ans, beg = ans[::-1],0
        while beg <len(ans) and ans[beg] == 0:
            beg +=1
        ans = map(str, ans[beg:])
        return "".join(ans)