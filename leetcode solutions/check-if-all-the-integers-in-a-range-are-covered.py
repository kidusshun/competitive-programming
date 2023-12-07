class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for j in range(left, right+1):
            covered = False
            for start,end in ranges:
                if start <= j <= end:
                    covered = True
            if not covered:
                return False
        return True