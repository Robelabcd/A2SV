class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        b = list(s.split())
        
        return len(b[-1])