class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque([char for char in senate])
        r_adv = 0
        d_adv = 0

        while len(q)>1 and r_adv < len(q) and d_adv < len(q):
            curr = q.popleft()
            if curr == "R" and d_adv>0:
                d_adv -=1
            elif curr == "R":
                r_adv +=1
                q.append(curr)
            elif curr == "D" and r_adv >0:
                r_adv-=1
            else:
                d_adv+=1
                q.append(curr)
        if q[0] == "R":
            return "Radiant"
        return "Dire"