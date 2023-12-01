class Solution:
    def romanToInt(self, s: str) -> int:
        prev = None
        ans = 0
        for char in s:
            if char == 'I':
                curr = 1
            elif char == 'V':
                curr = 5
            elif char == 'X':
                curr = 10
            elif char == 'L':
                curr = 50
            elif char == 'C':
                curr = 100
            elif char == 'D':
                curr = 500
            elif char == 'M':
                curr = 1000
            if prev == None:
                prev = curr
                ans +=curr
            elif curr <= prev:
                ans += curr
                prev = curr
            else:
                ans -= prev
                new = curr - prev
                ans += new
                prev = curr
        return ans