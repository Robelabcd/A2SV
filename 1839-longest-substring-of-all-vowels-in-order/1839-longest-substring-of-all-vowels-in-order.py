class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        lp = 0
        count = 0
        arr = set(word[lp])
        for rp in range(1, len(word)):

            if word[rp] < word[rp-1]:

                lp = rp
                arr = set(word[lp])

            arr.add(word[rp])

            if len(arr) == 5:
                count = max(count, rp-lp+1)

        return count


