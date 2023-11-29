class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def ternary (n):
            if n == 0:
                return '0'
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            return ''.join(reversed(nums))
        if "2" in ternary(n): return False
        return True