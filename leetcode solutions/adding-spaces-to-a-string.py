class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaced_string = ""
        prev = 0
        for pos in spaces:
            spaced_string+=(s[prev:pos] + " ")
            prev = pos
        spaced_string+=s[prev:]
        return spaced_string.rstrip()