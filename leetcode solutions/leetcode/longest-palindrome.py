class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        isOdd = False
        length = 0
        for key, val in count.items():
            if val%2==0:
                length+=val
            else:
                isOdd = True
                length += val-1
        if isOdd:
            return length +1
        return length