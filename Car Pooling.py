class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        endP = max(trips, key = lambda x: x[2])[2]
        a = [0] * (endP+1)

        for person, start, end in trips:
            a[start] += person
            a[end] -= person
        
        on = 0

        for num in a:
            on += num
            if on > capacity:
                return False
        return True