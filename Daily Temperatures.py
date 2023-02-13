class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and  temp > stack[-1][0]:
                stack_temp,stack_ind=stack.pop()
                ans[stack_ind]=(i-stack_ind)
            stack.append([temp,i])
        return ans