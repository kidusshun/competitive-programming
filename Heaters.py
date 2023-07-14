class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = float("-inf")
        length = len(heaters)
        heaters.sort()

        for house in houses:
            current_dist = abs(self.findClosest(heaters,length,house) - house)
            ans = max(ans, current_dist)
        
        return ans
        
    
    def findClosest(self, heaters, length, house):
        if house <= heaters[0]:
            return heaters[0]
        elif house >= heaters[-1]:
            return heaters[-1]
        
        i = 0
        j = length - 1
        result = 0

        while i <= j:
            mid = (i+j)//2
            if abs(heaters[mid] - house) < abs(heaters[result] - house):
                    result = mid

            if heaters[mid] == house:
                return heaters[mid] 
            
            elif heaters[mid] < house:
                i = mid + 1
            elif heaters[mid] > house:
                j = mid - 1
        
        return heaters[result]