class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # Check if the rearrangement is possible
        max_freq = sorted_chars[0][1]
        if max_freq > (len(s) + 1) // 2:
            return ""  # Impossible to rearrange
        
        
        result = [None] * len(s)
        
        #Fill even indices first, then odd indices
        index = 0
        for char, freq in sorted_chars:
            for _ in range(freq):
                result[index] = char
                index += 2
                if index >= len(s):
                    index = 1
        
        return ''.join(result)