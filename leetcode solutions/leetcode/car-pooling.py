class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0]*(max(trips, key = lambda x:x[2])[2]+1)
        for trip in trips:
            car[trip[1]] +=trip[0]
            car[trip[2]] -=trip[0]
        for i in range(1,len(car)):
            car[i] += car[i-1]
            if car[i]> capacity:
                return False
        
        if car[0]>capacity:return False
        return True