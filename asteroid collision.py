class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans =[]
        for n in asteroids:
            if not ans or n>0:
                ans.append(n)
            else:
                while ans and n<0 and ans[-1]>0 and ans[-1] < abs(n):
                    ans.pop()
                if not ans or ans[-1] < 0:
                    ans.append(n)
                elif ans[-1] == abs(n):
                    ans.pop()
        return ans