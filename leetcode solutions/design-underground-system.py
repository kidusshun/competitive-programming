class UndergroundSystem:

    def __init__(self):
        self.checkIns = defaultdict(tuple)
        self.checkouts =defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkouts[f"{stationName} {self.checkIns[id][0]}"].append(t-self.checkIns[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.checkouts[f"{endStation} {startStation}"])/len(self.checkouts[f"{endStation} {startStation}"])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)