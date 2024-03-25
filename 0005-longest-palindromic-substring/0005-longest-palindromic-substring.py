class Solution:
    def longestPalindrome(self, s: str) -> str:
        letters = list(s)
        maximum = 0
        for i in range(len(letters)):
            for j in range(i + maximum, len(letters)):
                subarray = letters[i: j + 1]
                left = 0
                right = len(subarray) - 1
                while left < right:
                    if subarray[right] != subarray[left]:
                        break
                    right -= 1
                    left += 1
                else:
                    maximum = j - i + 1
                    answer = subarray

        return "".join(answer)
  