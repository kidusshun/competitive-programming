class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        d = Counter(arr)
        for key, val in d.items():
            if val/length>0.25:
                return key