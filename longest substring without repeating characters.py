class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind1,ind2=0,0
        sub=s[ind1:ind2]
        max=0
        while ind2<len(s):
            if s[ind2] not in sub:
                ind2+=1
                sub=s[ind1:ind2]
            elif s[ind2] in sub:
                ind1+=1
                sub=s[ind1:ind2]
            else:
                ind1+=1
                ind2+=1
            if len(sub)>max:
                max=len(sub)
        return max



