class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0]*(n+1)
        for booking in bookings:
            answer[booking[0]-1]+= booking[2]
            answer[booking[1]]-= booking[2]

        return list(accumulate(answer[:-1]))