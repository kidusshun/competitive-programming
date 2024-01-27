class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(len(bookings)):
            ans[bookings[i][0]-1] +=bookings[i][2]
            ans[bookings[i][1]] -=bookings[i][2]
        for i in range(1,n):
            ans[i]+=ans[i-1]
        ans.pop()
        return ans