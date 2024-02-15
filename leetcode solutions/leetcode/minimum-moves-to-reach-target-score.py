class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = target
        ops = 0
        while maxDoubles >0 and curr>1:
            quot, rem = divmod(curr,2)
            ops += rem+1
            curr = quot
            maxDoubles -=1
        return ops + (curr - 1)