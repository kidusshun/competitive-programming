class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        max_area=0
        left=0
        while left<len(height):
            area=(right-left)* min(height[left],height[right])
            max_area=max(area,max_area)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area