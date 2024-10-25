class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()
    
        gcdd = reduce(gcd, count)
        
        return gcdd > 1
