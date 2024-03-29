class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i,j):
            if i>=j:
                return
            s[i],s[j] = s[j],s[i]
            helper(i+1,j-1)
        helper(0,len(s)-1)