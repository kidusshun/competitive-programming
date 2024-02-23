class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        curr = 0
        for i in range(len(height)):
            
            while stack and height[i] >= stack[0][0]:
                popped = stack.pop()
                ans += popped[1]
            if stack:
                curr = (stack[0][0]-height[i])        
            else:
                curr = 0    
            stack.append((height[i],curr))

        print(stack)
        if stack:
            max_ = stack.pop()
        while stack:
            curr = stack.pop()
            if max_[0]>curr[0]:
                ans+=max_[0]-curr[0]
            else:
                max_ = curr            
        return ans