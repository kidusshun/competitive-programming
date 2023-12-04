class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        length = 0
        if start < destination:
            for i in range(start, destination):
                length += distance[i]
            return min(length, sum(distance) - length)
        else:
            for i in range(destination, start):
                length += distance[i]
            return min(length, sum(distance) - length)