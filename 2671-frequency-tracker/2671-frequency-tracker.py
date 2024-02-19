class FrequencyTracker(object):
    def __init__(self):
        self.s=defaultdict(int)
        self.t=defaultdict(int)

    def add(self, number):
       
        self.t[self.s[number]]-=1
        self.s[number]+=1
        self.t[self.s[number]]+=1
        

    def deleteOne(self, number):
        
        if self.s[number]>0:
            self.t[self.s[number]]-=1
            self.s[number]-=1
            self.t[self.s[number]]+=1    

    def hasFrequency(self, frequency):
        
        return self.t[frequency]>0
        

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)