class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count("0")
        ones = s.count("1")
        ones_seen = 0
        zeros_seen = 0
        ans = 0
        for char in s:
            if char == "0":
                zeros-=1
                zeros_seen+=1
                ans+= ones*ones_seen
            else:
                ones-=1
                ones_seen +=1
                ans+= zeros*zeros_seen
        return ans