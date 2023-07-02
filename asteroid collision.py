class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans=[]
        for num in asteroids:
            if len(ans) == 0:
                ans.append(num)
            elif ans[-1] >= num and ((num > 0 and ans[-1] < 0) or (num < 0 and ans[-1] > 0)):
                if abs(num) >= abs(ans[-1]):
                    while len(ans)>0 and ans[-1] >= num and ((num > 0 and ans[-1] < 0) or (num < 0 and ans[-1] > 0)):
                        if abs(num) >= abs(ans[-1]):
                            ans.pop()
                        else:
                            break
                        
                        
            else:
                ans.append(num)
        return ans
s = Solution()
s.asteroidCollision([-2,-2,1,-2])