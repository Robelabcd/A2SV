class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
           "I" : 1,
           "V" : 5,
           "X" : 10,
           "L" : 50,
           "C" : 100,
           "D" : 500,
           "M" : 1000
        }

        ans = 0
        n, i = len(s), 0

        while i < n:
            if i < n-1 and roman_value[s[i]] < roman_value[s[i+1]]:
                value = roman_value[s[i+1]] - roman_value[s[i]]
                ans += value
                i += 2

            else:
                value = roman_value[s[i]]
                ans += value
                i += 1

        return ans


