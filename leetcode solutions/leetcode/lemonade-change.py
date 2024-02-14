class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0,0,0]
        for num in bills:
            if num == 5:
                changes[0] +=1
            elif num == 10:
                changes[1]+=1
                if changes[0]>0:
                    changes[0]-=1
                else:
                    return False
            else:
                changes[2]+=1
                if changes[1] > 0 and changes[0] > 0:
                    changes[1] -= 1
                    changes[0] -= 1
                elif changes[0] >=3:
                    changes[0] -= 3
                else:
                    return False
        return True