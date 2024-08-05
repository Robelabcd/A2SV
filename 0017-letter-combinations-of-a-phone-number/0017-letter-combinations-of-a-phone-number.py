class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #DO it again if you encounter this problem
        
        
        res = []
        dicts = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}
        combo = []

        def combos_function(i):
            if i == len(digits):
                res.append(''.join(combo))
                return

            for letter in dicts[digits[i]]:
                combo.append(letter)
                combos_function(i + 1)
                combo.pop()

        if digits:
            combos_function(0)

        return res
  