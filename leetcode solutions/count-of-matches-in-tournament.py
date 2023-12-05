class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        matches = 0
        while teams > 1:
            if teams%2 != 0:
                match = (teams+1)//2
                teams = match
                matches+=match-1
            else:
                match = teams //2
                matches+=match
                teams = match
        return matches