class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sett = set()

        left_pointer = 0
        
        length = 0

        for right_pointer in range(len(s)):

            while s[right_pointer] in sett:

                sett.remove(s[left_pointer])

                left_pointer += 1

            sett.add(s[right_pointer])
            length = max(length, right_pointer - left_pointer + 1)

        return length

# time complexity : O(n) - because both the pointer iterates atmost n times

# space complexity : O(n) - since the set contains n elements


