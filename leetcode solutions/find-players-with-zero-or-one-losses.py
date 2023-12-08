class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        more_lose = set()
        d = {0:set(),1:set()}
        for win, lose in matches:
            if win not in d[0] and win not in d[1] and win not  in more_lose:
                d[0].add(win)
            if lose not in d[0] and lose not in d[1] and lose not in more_lose:
                d[1].add(lose)
            elif lose  in d[0]:
                d[0].remove(lose)
                d[1].add(lose)
            elif lose in d[1]:
                d[1].remove(lose)
                more_lose.add(lose)
        wins = list(d[0])
        loses = list(d[1])
        final_answer = [sorted(wins),sorted(loses)]
        return final_answer