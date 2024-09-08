class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        arr = [0] * len(words)
        for i in range(len(words)):
            bitmask = 0
            for j in words[i]:
                bitmask |= 1 << (ord(j) - ord('a'))
            arr[i] = bitmask
        max_product = 0  
        for i in range(len(words)):
            for j in range(1, len(words)):
                if arr[i] & arr[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product