class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word = Counter(s1)
        window = Counter(s2[:len(s1)-1])
        l = 0

        for r in range(len(s1)-1,len(s2)):
            window[s2[r]] +=1
            if word == window:
                return True
            
            window[s2[l]] -= 1
            if not window[s2[l]]:
                del window[s2[l]]
            l+=1
        return False