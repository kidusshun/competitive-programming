class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n ==1:
            return 0
        def recursive(k,level):
            if level == 1: 
                return 0
            val = recursive((k+1)//2,level-1)
            if k%2==0:
                if val == 1:
                    return 0
                return 1
            else:
                return val

        return recursive(k,n)