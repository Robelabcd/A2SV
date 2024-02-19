class UndergroundSystem(object):

    def __init__(self):
        self.travelers_hm = {}
        self.location_duration_hm = {}
        

    def checkIn(self, id, stationName, t):
        
        self.travelers_hm[id] = [stationName, t]
        

    def checkOut(self, id, stationName, t):
        
        if id in self.travelers_hm:
            start_station = self.travelers_hm[id][0]
            travel_duration = t - self.travelers_hm[id][1]
            if (start_station, stationName) in self.location_duration_hm:
                self.location_duration_hm[(start_station, stationName)].append(travel_duration)
            else:
                self.location_duration_hm[(start_station, stationName)] = [travel_duration]
        

    def getAverageTime(self, startStation, endStation):
        
        travel_duration_list = self.location_duration_hm[(startStation, endStation)]
        return sum(travel_duration_list) / float(len(travel_duration_list))

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)