class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def slide(s):
            i,j = 0,0
            curr = k
            ans = 0
            while j<len(s):
                if s[j]=='T':
                    ans = max(ans,j-i+1)
                elif curr>0:
                    ans = max(ans,j-i+1)
                    curr-=1
                else:
                    while s[i] =='T':
                        i+=1
                    i+=1
                    ans = max(ans,j-i+1)
                j+=1
            return ans
        rev = "".join('F' if x=='T' else 'T' for x in answerKey)
        return max(slide(answerKey),slide(rev))