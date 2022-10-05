"""
customer -> hmap/dict -> with basically starting times, and then may be I can delete it later on.
stations -> store total time travelled for every customer

"""



class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.customers[id]
        self.stations[(station, stationName)].append(t-time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stations[(startStation, endStation)])/len(self.stations[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)