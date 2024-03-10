class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        check = False
        for i in range(len(haystack) - len(needle) + 1):

            if haystack[i] == needle[0]:
        
                check = True if (haystack[i:i + len(needle)]) == needle else False

            if check:
                return i

        return -1