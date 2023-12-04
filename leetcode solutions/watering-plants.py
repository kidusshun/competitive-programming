class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        curr = capacity
        for i,plant in enumerate(plants):
            if plant <= curr:
                curr-=plant
                ans+=1
            else:
                curr = capacity
                ans+= (i+i+1)
                curr -= plant
        return ans