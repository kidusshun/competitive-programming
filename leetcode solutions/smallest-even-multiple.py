class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        curr = n
        while curr%2 != 0:
            curr *=2
        return curr
        