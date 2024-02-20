class AuthenticationManager(object):

    def __init__(self, timeToLive):
       
        self.tokens = dict()
        self.time = timeToLive       

    def generate(self, tokenId, currentTime):
        
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId, currentTime):
        
        limit = currentTime - self.time
        if tokenId in self.tokens and self.tokens[tokenId] > limit:
            self.tokens[tokenId] = currentTime

        

    def countUnexpiredTokens(self, currentTime):
        
        c = 0
        limit = currentTime - self.time
        for tid in self.tokens:
            if self.tokens[tid] > limit:
                c += 1
        return c 
        

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)