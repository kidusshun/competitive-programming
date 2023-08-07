class Solution:
    def largestInteger(self, num: int) -> int:
        odds = []
        even = []
        string = str(num)

        for nu in string:
            integer = int(nu)
            if integer%2 == 0:heapq.heappush(even,integer)
            else: heapq.heappush(odds,integer)
        
        ans = ""
        for char in string[::-1]:
            if int(char)%2 == 0:
                ans+= str(heappop(even))
            else:
                ans+= str(heappop(odds))
        return int(ans[::-1])