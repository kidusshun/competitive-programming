class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num//3
        if 3*mid == num:
            return [mid-1,mid,mid+1]
        return []