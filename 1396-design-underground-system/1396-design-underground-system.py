"""
customer -> hmap/dict -> with basically starting times, and then may be I can delete it later on.
stations -> store total time travelled for every customer

"""



class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.customers[id]
        if (station, stationName) in self.stations:
            self.stations[(station, stationName)][0]+=t-time
            self.stations[(station, stationName)][1]+=1
        else:
            self.stations[(station, stationName)] = [t-time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[(startStation, endStation)][0]/self.stations[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)