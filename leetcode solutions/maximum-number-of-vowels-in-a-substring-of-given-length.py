class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set({'a','e', 'i', 'o', 'u'})
        count = 0
        i = 0
        max_ = 0
        for j in range(k):
            if s[j] in vowels:
                max_ +=1
                count +=1
        for j in range(k,len(s)):
            if s[i] in vowels:
                count-=1
            i+=1
            if s[j] in vowels:
                count+=1
            j+=1
            max_ = max(max_, count)
        return max_