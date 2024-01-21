class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        offset = [0]*(len(s)+1)
        for start,end, direction in shifts:
            if direction == 1:
                offset[start] +=1
                offset[end+1] -=1
            else:
                offset[start] -=1
                offset[end+1] +=1
        for i in range(1,len(s)):
            offset[i] += offset[i-1]
        ans = ""
        for i,char in enumerate(s):
            curr = (ord(char) - 97 + offset[i])%26
            ans += chr(curr+97)
        return ans